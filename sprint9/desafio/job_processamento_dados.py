import sys
import boto3
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from awsglue.transforms import *  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.context import SparkContext
from pyspark.sql.functions import col,explode,trim,expr  # type: ignore

# @params: [JOB_NAME, S3_CSV_INPUT_PATH, S3_JSON_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_CSV_INPUT_PATH', 'S3_JSON_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# # CONSTANTES

# datalake-pedro-silva/Trusted/job_json/
DIRETORIO_JSON = args['S3_JSON_INPUT_PATH']

# datalake-pedro-silva/Trusted/job_csv/
DIRETORIO_CSV = args['S3_CSV_INPUT_PATH']

# s3://pedro-silva-desafio/datalake-pedro-silva/Refined/
DIRETORIO_FINAL = args['S3_TARGET_PATH']
BUCKET = 'pedro-silva-desafio'


def arquivo_mais_recente(bucket: str, prefix: str):
    '''
    Encontrar o arquivo Parquet mais recente em um bucket S3, navegando pelos diretórios organizados por ano/mês/dia.
    Caso não haja subdiretórios, encontrar o arquivo Parquet mais recente dentro do diretório atual.

    :param bucket: Nome do bucket S3.
    :param prefix: Prefixo do diretório base no bucket S3.
    :return: Endereço do S3 com o Parquet mais recente.
    '''

    s3_client = boto3.client('s3')

    # Função para listar arquivos e diretórios com prefixo
    def listar(prefix):
        response = s3_client.list_objects_v2(
            Bucket=bucket, Prefix=prefix, Delimiter='/')
        return response.get('CommonPrefixes', []), response.get('Contents', [])

    # Navega pelos diretórios até encontrar o mais recente
    while True:
        diretorios, arquivos = listar(prefix)

        if diretorios:
            # Obter o diretório mais recente
            prefix = max(diretorios, key=lambda d: d['Prefix'])['Prefix']
        elif arquivos:
            # Se não há mais subdiretórios, procurar pelo arquivo Parquet mais recente
            arquivos_parquet = [
                a for a in arquivos if a['Key'].endswith('.parquet')]
            if not arquivos_parquet:
                raise Exception(f"No Parquet files found in {bucket}/{prefix}")
            # Encontrar o arquivo mais recente
            arquivo_mais_recente = max(
                arquivos_parquet, key=lambda x: x['LastModified'])
            return f"s3://{bucket}/{arquivo_mais_recente['Key']}"
        else:
            raise Exception(
                f"No directories or Parquet files found in {bucket}/{prefix}")


# Carrega os arquivos
csv_parquet = arquivo_mais_recente(BUCKET, DIRETORIO_CSV)
json_parquet = arquivo_mais_recente(BUCKET, DIRETORIO_JSON)

df_csv = spark.read.format('parquet').options(
    header=True, inferSchema=True).load(csv_parquet)

df_json = spark.read.format('parquet').options(
    header=True, inferSchema=True).load(json_parquet)

df_csv = df_csv.withColumnRenamed("tituloPincipal", "titulo")
# -----------------------------------------------------------------------

# Criando Tabelas

# Unindo CSV e JSON em um único dataframe
df_completo = df_csv.join(
    df_json, df_csv["titulo"] == df_json["titulo"], "left_outer")

# Fato - Filme ----------------------------------------------------------

df_fato_filme = df_completo.select(
    df_csv["id"].alias("id"),
    df_csv["titulo"].alias("titulo"),
    df_csv["notaMedia"].alias("nota_media").cast("float"),
    df_csv["numeroVotos"].alias("numero_votos").cast("integer"),
    df_json["popularidade"].alias("popularidade").cast("integer"),
    df_json["orcamento"].alias("orcamento").cast("integer"),
    df_json["bilheteria"].alias("bilheteria").cast("integer"),
    df_csv["tempoMinutos"].alias("duracao").cast("integer")
)

df_fato_filme = df_fato_filme.distinct()

# Dimensão - Tempo ------------------------------------------------------

df_dim_tempo = df_completo.select(
    df_csv["id"].alias("id"),
    df_csv['anoLancamento'].alias("ano_lancamento")
)

df_dim_tempo= df_dim_tempo.distinct()

# Dimensão - Gênero ------------------------------------------------------

# Explodir a array de gêneros em múltiplas linhas (um gênero por linha)
df_dim_generos_explode = df_completo.select(
    df_csv["id"].alias("id"),
    df_csv['genero'].alias('genero')
).withColumn(
    "genero_explodido", explode(col("genero")))

# ------------------------------------------------------------------------

# Remover espaços em branco e duplicatas
df_dim_generos_unicos = df_dim_generos_explode.select(
    trim(col("genero_explodido")).alias("nome")).distinct()

# Adicionar um ID único para cada gênero
df_dim_genero = df_dim_generos_unicos.withColumn(
    "id", expr("row_number() over (order by nome)"))

# Bridge - Filmes_Generos ------------------------------------------------------

# Remover espaços em branco
df_filmes_generos_explode = df_dim_generos_explode.withColumn(
    "genero_explodido", trim(col("genero_explodido"))
)

# Realizar o join com a dim_genero para obter o id
df_bridge_filmes_genero = df_filmes_generos_explode.join(
    df_dim_genero,
    df_filmes_generos_explode["genero_explodido"] == df_dim_genero["nome"],
    "inner"
).select(
    df_filmes_generos_explode["id"].alias("id_filme"),
    df_dim_genero["id"].alias("id_genero")
).distinct()

# Dimensão - Produtora ------------------------------------------------------

# Explodir a array de gêneros em múltiplas linhas (um gênero por linha)
df_dim_produtoras_explode = df_completo.select(
    df_csv["id"].alias("id"),
    df_json['produtoras'].alias('produtoras')
).withColumn(
    "produtora_explodido",  explode(col("produtoras")))

# ------------------------------------------------------------------------

# Remover espaços em branco e duplicatas
df_dim_produtoras_unicas = df_dim_produtoras_explode.select(
    trim(col("produtora_explodido")).alias("nome")).distinct()

# Adicionar um ID único para cada produtora
df_dim_produtora = df_dim_produtoras_unicas.withColumn(
    "id", expr("row_number() over (order by nome)"))

# Bridge - Filmes_Produtora ------------------------------------------------------

# Remover espaços em branco
df_filmes_produtoras_explode = df_dim_produtoras_explode.withColumn(
    "produtora_explodido", trim(col("produtora_explodido"))
)

# Realizar o join com a dim_produtora para obter o id
df_bridge_filmes_produtora = df_filmes_produtoras_explode.join(
    df_dim_produtora,
    df_filmes_produtoras_explode["produtora_explodido"] == df_dim_produtora["nome"],
    "inner"
).select(
    df_filmes_produtoras_explode["id"].alias("id_filme"),
    df_dim_produtora["id"].alias("id_produtora")
).distinct()


# Dimensão - Palavras-chave ------------------------------------------------------

# Explodir a array de palavras_chave em múltiplas linhas (um gênero por linha)
df_dim_palavras_chave_explode = df_completo.select(
    df_csv["id"].alias("id"),
    df_json['palavras_chave'].alias('palavra_chave')
).withColumn(
    "palavra_chave_explodido",  explode(col("palavra_chave")))

# ------------------------------------------------------------------------

# Remover espaços em branco e duplicatas
df_dim_palavras_chave_unicas = df_dim_palavras_chave_explode.select(
    trim(col("palavra_chave_explodido")).alias("nome")).distinct()

# Adicionar um ID único para cada palavra chave
df_dim_palavra_chave = df_dim_palavras_chave_unicas.withColumn(
    "id", expr("row_number() over (order by nome)"))

# Bridge - Filmes_Palaras_chave ------------------------------------------------------

# Remover espaços em branco
df_filmes_palavra_chave_explode = df_dim_palavras_chave_explode.withColumn(
    "palavra_chave_explodido", trim(col("palavra_chave_explodido"))
)

# Realizar o join com a dim_palavra_chave para obter o id
df_bridge_filmes_palavra_chave = df_filmes_palavra_chave_explode.join(
    df_dim_palavra_chave,
    df_filmes_palavra_chave_explode["palavra_chave_explodido"] == df_dim_palavra_chave["nome"],
    "inner"
).select(
    df_filmes_palavra_chave_explode["id"].alias("id_filme"),
    df_dim_palavra_chave["id"].alias("id_palavra_chave")
).distinct()


'''
# Etapa de Testes -------------------------------------------------------------------
df_fato_filme.show(30)

df_dim_tempo.show(30)

df_dim_genero.show(30)
df_bridge_filmes_genero.show(30)

df_dim_produtora.show(30, truncate=False)
df_bridge_filmes_produtora.show(30)

df_dim_palavra_chave.show(30, truncate=False)
df_bridge_filmes_palavra_chave.show(30)

'''

# Escrever no S3 em formato parquet

df_fato_filme.write.mode("overwrite"
                         ).parquet(f'{DIRETORIO_FINAL}/fato_filme')

df_dim_tempo.write.mode("overwrite"
                        ).parquet(f'{DIRETORIO_FINAL}/dim_tempo')

df_dim_genero.write.mode("overwrite"
                         ).parquet(f'{DIRETORIO_FINAL}/dim_genero')

df_bridge_filmes_genero.write.mode("overwrite"
                                   ).parquet(f'{DIRETORIO_FINAL}/bridge_filmes_genero')

df_dim_produtora.write.mode("overwrite"
                            ).parquet(f'{DIRETORIO_FINAL}/dim_produtora')

df_bridge_filmes_produtora.write.mode("overwrite"
                                      ).parquet(f'{DIRETORIO_FINAL}/bridge_filmes_produtora')

df_dim_palavra_chave.write.mode("overwrite"
                                ).parquet(f'{DIRETORIO_FINAL}/dim_palavra_chave')

df_bridge_filmes_palavra_chave.write.mode("overwrite"
                                          ).parquet(f'{DIRETORIO_FINAL}/bridge_filmes_palavra_chave')


job.commit()
