import sys
import boto3
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from awsglue.transforms import *  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.context import SparkContext
from pyspark.sql.functions import col, array_contains, split

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# datalake-pedro-silva/Raw/Local/CSV/movies/
DIRETORIO_CSV = args['S3_INPUT_PATH']

# datalake-pedro-silva/Trusted/job_csv/
DIRETORIO_FINAL = args['S3_TARGET_PATH']

BUCKET = 'pedro-silva-desafio'

def csv_mais_recente(bucket: str, prefix: str):
    '''
    Encontrar o CSV mais recente em um bucket S3 com diretórios organizados por ano/mês/dia.

    :param bucket: Nome do bucket S3.
    :param prefix: Prefixo do diretório base no bucket S3.
    :return: Endereço do S3 com o CSV mais recente.
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

    # Obter arquivos CSV dentro do dia mais recente
    response = listar(dia_mais_recente_prefixo)
    arquivos_csv = [a for a in response.get(
        'Contents', []) if a['Key'].endswith('.csv')]

    if not arquivos_csv:
        raise Exception(
            f"No CSV files found in {bucket}/{dia_mais_recente_prefixo}")

    # Encontrar o arquivo CSV mais recente
    arquivo_mais_recente = max(arquivos_csv, key=lambda x: x['LastModified'])
    return f"s3://{bucket}/{arquivo_mais_recente['Key']}"

# Carrega o arquivo CSV 
arquivo = csv_mais_recente(BUCKET, DIRETORIO_CSV)

df = spark.read.format("csv").option(
    "header", "true").option("delimiter", "|").load(arquivo)

# Filtrar linhas onde o ano está entre 1980 e 1999 e o gênero contém 'Sci-Fi'
df = df.withColumn("anoLancamento", col("anoLancamento").cast("int"))
df = df.withColumn("genero", split(col("genero"), ","))

df_filtrado = df.filter((col("anoLancamento").between(1980, 1999)) & (
    array_contains(col("genero"), "Sci-Fi")))

# Escrever no S3 em formato parquet
df_filtrado.coalesce(1).write.mode("overwrite").parquet(DIRETORIO_FINAL)

job.commit()
