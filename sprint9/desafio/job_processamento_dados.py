from pyspark.sql.functions import *  # type: ignore
from pyspark.sql import SparkSession  # type: ignore

# import sys
# import boto3
# from awsglue.context import GlueContext  # type: ignore
# from awsglue.job import Job  # type: ignore
# from awsglue.transforms import *  # type: ignore
# from awsglue.utils import getResolvedOptions  # type: ignore
# from pyspark.context import SparkContext
# from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType

# # @params: [JOB_NAME, S3_CSV_INPUT_PATH, S3_JSON_INPUT_PATH, S3_TARGET_PATH]
# args = getResolvedOptions(
#     sys.argv, ['JOB_NAME', 'S3_CSV_INPUT_PATH', 'S3_JSON_INPUT_PATH', 'S3_TARGET_PATH'])

# # Inicializa o contexto do Glue e Spark
# sc = SparkContext()
# glueContext = GlueContext(sc)
# spark = glueContext.spark_session
# job = Job(glueContext)
# job.init(args['JOB_NAME'], args)

# # CONSTANTES

# # s3://pedro-silva-desafio/datalake-pedro-silva/Trusted/job_json/
# DIRETORIO_JSON = args['S3_JSON_INPUT_PATH']

# # s3://pedro-silva-desafio/datalake-pedro-silva/Trusted/job_csv/
# DIRETORIO_CSV = args['S3_CSV_INPUT_PATH']

# # s3://pedro-silva-desafio/datalake-pedro-silva/Refined/
# DIRETORIO_FINAL = args['S3_CSV_TARGET_PATH']
# BUCKET = 'pedro-silva-desafio'


def arquivo_mais_recente(bucket: str, prefix: str):
    '''
    Encontrar o arquivo Parquet mais recente em um bucket S3 com diretórios organizados por ano/mês/dia.

    :param bucket: Nome do bucket S3.
    :param prefix: Prefixo do diretório base no bucket S3.
    :return: Endereço do S3 com o Parquet mais recente.
    '''

    s3_client = boto3.client('s3')

    # Função para listar arquivos e diretórios com prefixo
    def listar(prefix):
        return s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter='/')

    # Encontrar o diretório mais recente
    def encontrar_mais_recente(diretórios):
        return max(diretórios, key=lambda d: d['Prefix'])['Prefix']

    # Obter o ano mais recente
    response = listar(prefix)
    ano_mais_recente_prefixo = encontrar_mais_recente(
        response.get('CommonPrefixes', []))

    # Obter o mês mais recente dentro do ano mais recente
    response = listar(ano_mais_recente_prefixo)
    mes_mais_recente_prefixo = encontrar_mais_recente(
        response.get('CommonPrefixes', []))

    # Obter o dia mais recente dentro do mês mais recente
    response = listar(mes_mais_recente_prefixo)
    dia_mais_recente_prefixo = encontrar_mais_recente(
        response.get('CommonPrefixes', []))

    # Obter arquivos JSON dentro do dia mais recente
    response = listar(dia_mais_recente_prefixo)
    arquivo = [a for a in response.get(
        'Contents', []) if a['Key'].endswith('.parquet')]

    if not arquivo:
        raise Exception(
            f"No files found in {bucket}/{dia_mais_recente_prefixo}")

    # Encontrar o arquivo mais recente
    arquivo_mais_recente = max(arquivo, key=lambda x: x['LastModified'])

    return f"s3://{bucket}/{arquivo_mais_recente['Key']}"


# Carrega os arquivos
csv_parquet = './csv.parquet'  # arquivo_mais_recente(BUCKET, DIRETORIO_JSON)
json_parquet = './json.parquet'  # arquivo_mais_recente(BUCKET, DIRETORIO_CSV)

# Iniciar sessão
spark = SparkSession.builder \
    .appName("testeSprint9") \
    .getOrCreate()

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
    df_csv["notaMedia"].alias("notaMedia"),
    df_csv["numeroVotos"].alias("numero_votos"),
    df_json["popularidade"].alias("popularidade"),
    df_json["orcamento"].alias("orcamento"),
    df_json["bilheteria"].alias("bilheteria"),
    df_csv["tempoMinutos"].alias("duracao")
)

# Dimensão - Tempo ------------------------------------------------------

df_dim_tempo = df_completo.select(
    df_csv["id"].alias("id"),
    df_csv['anoLancamento'].alias("ano_lancamento")
)

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

# Etapa de Testes -------------------------------------------------------------------

df_fato_filme.show(30)

df_dim_tempo.show(30)

df_dim_genero.show(30)
df_bridge_filmes_genero.show(30)

df_dim_produtora.show(30, truncate=False)
df_bridge_filmes_produtora.show(30)

df_dim_palavra_chave.show(30,truncate=False)
df_bridge_filmes_palavra_chave.show(30)


# Escrever no S3 em formato parquet

# df.write.mode("overwrite").parquet(DIRETORIO_FINAL)

# job.commit()
