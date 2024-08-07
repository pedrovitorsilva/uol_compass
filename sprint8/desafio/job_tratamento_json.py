from datetime import datetime
import sys
import boto3
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from awsglue.transforms import *  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.context import SparkContext
from pyspark.sql.functions import col, array_contains, split
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# datalake-pedro-silva/Raw/TMDB/JSON/
DIRETORIO_JSON = args['S3_INPUT_PATH']

DATA_DE_PROCESSAMENTO = datetime.today().strftime('%Y/%m/%d')

# s3://pedro-silva-desafio/datalake-pedro-silva/Trusted/job_json/ano/mes/dia
DIRETORIO_FINAL = f"{args['S3_TARGET_PATH']}/{DATA_DE_PROCESSAMENTO}"

BUCKET = 'pedro-silva-desafio'


def json_mais_recente(bucket: str, prefix: str):
    '''
    Encontrar o JSON mais recente em um bucket S3 com diretórios organizados por ano/mês/dia.

    :param bucket: Nome do bucket S3.
    :param prefix: Prefixo do diretório base no bucket S3.
    :return: Endereço do S3 com o JSON mais recente.
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
    arquivo_json = [a for a in response.get(
        'Contents', []) if a['Key'].endswith('.json')]

    if not arquivo_json:
        raise Exception(
            f"No JSON files found in {bucket}/{dia_mais_recente_prefixo}")

    # Encontrar o arquivo CSV mais recente
    arquivo_mais_recente = max(arquivo_json, key=lambda x: x['LastModified'])

    return f"s3://{bucket}/{arquivo_mais_recente['Key']}"


# Carrega o arquivo JSON
arquivo = json_mais_recente(BUCKET, DIRETORIO_JSON)

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("titulo", StringType(), True),
    StructField("produtoras", ArrayType(StringType()), True),
    StructField("popularidade", FloatType(), True),
    StructField("orcamento", IntegerType(), True),
    StructField("bilheteria", IntegerType(), True),
    StructField("palavras_chave", ArrayType(StringType()), True)
])

df = spark.read.option("multiline", "true").schema(schema).json(arquivo)

# Escrever no S3 em formato parquet
df.write.mode("overwrite").parquet(DIRETORIO_FINAL)

job.commit()
