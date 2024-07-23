# Script usado no AWS Glue, para execução de um job

import sys
from awsglue.transforms import *  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.context import SparkContext  # type: ignore
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from pyspark.sql.functions import col, upper, count  # type: ignore
import boto3
import io
import pandas as pd

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Criar um buffer para armazenar os logs
log_buffer = io.StringIO()


def log_message(message):
    print(message)
    log_buffer.write(message + "\n")


# Carrega o arquivo CSV
df = spark.read.format("csv").option("header", "true").load(source_file)

schema_str = df.schema.simpleString()
log_message("Schema do dataframe:\n" + schema_str)

df_maiusculo = df.withColumn("nome", upper(col("nome")))

# Imprimir
row_count = df_maiusculo.count()
log_message("Total de linhas no dataframe: {}".format(row_count))

df2 = df_maiusculo.groupBy("ano", "sexo").agg(count("nome").alias("contagem"))

# Imprimir
df2_pd = df2.toPandas()
log_message("Contagem agrupada por ano e sexo:\n" +
            df2_pd.to_string(index=False))

df3 = df_maiusculo.orderBy(col("ano").desc())

# Imprimir
df3_pd = df3.limit(20).toPandas()  # Limitar a 20 linhas para não sobrecarregar
log_message("Dados ordenados pelo ano (mais recente primeiro):\n" +
            df3_pd.to_string(index=False))

# Nome feminino com mais registros e o ano em que ocorreu
df_feminino = df_maiusculo.filter(col("sexo") == "F")
mulher_mais_recorrente = df_feminino.groupBy("ano", "nome").agg(
    count("nome").alias("contagem")).orderBy(col("contagem").desc()).first()

log_message(
    f"Nome feminino mais comum: {mulher_mais_recorrente['nome']} com {mulher_mais_recorrente['contagem']} registros em {mulher_mais_recorrente['ano']}")

# Nome masculino com mais registros e o ano em que ocorreu
df_masculino = df_maiusculo.filter(col("sexo") == "M")
homem_mais_comum = df_masculino.groupBy("ano", "nome").agg(
    count("nome").alias("contagem")).orderBy(col("contagem").desc()).first()

log_message(
    f"Nome masculino mais comum: {homem_mais_comum['nome']} com {homem_mais_comum['contagem']} registros em {homem_mais_comum['ano']}")

# Total de registros (masculinos e femininos) para cada ano
total_por_ano = df_maiusculo.groupBy("ano").agg(
    count("nome").alias("total_registros")).orderBy(col("ano").asc())

# Converte total_por_ano para pandas DataFrame e imprime
total_por_ano_pd = total_por_ano.limit(10).toPandas()  # Limitar a 10 linhas
log_message("Total de registros por ano (primeiras 10 linhas):\n" +
            total_por_ano_pd.to_string(index=False))

# Salvar arquivos ----------------------------------------------
df_maiusculo.write.partitionBy("sexo", "ano").mode(
    "overwrite").json(target_path)

# Escreve o log no S3
s3_client = boto3.client('s3')
bucket_name = target_path.split('/')[2]
key_name = '/'.join(target_path.split('/')[3:]) + "/logs.txt"
s3_client.put_object(Bucket=bucket_name, Key=key_name,
                     Body=log_buffer.getvalue())

job.commit()
