# ! pip install wget

from pyspark.sql.functions import explode, split, col  # type: ignore
from pyspark.sql import SparkSession  # type: ignore
import wget

arquivo = 'README.md'
# Atualizar link com token a cada uso (repositório privado)
url = "https://raw.githubusercontent.com/pedrovitorsilva/uol_compass/main/README.md?token=GHSAT0AAAAAACS256EFM7WT4ZPJDHUJEVRIZU2WW5Q"

wget.download(url, arquivo)

# Iniciar sessão
spark = SparkSession.builder \
    .appName("Contador") \
    .getOrCreate()

# Ler e processar arquivo
df = spark.read.text(arquivo)

numero_de_palavras = (
    df.withColumn('palavra', explode(split(col('value'), ' ')))
    .groupBy('palavra')
    .count()
    .sort('count', ascending=False)
)

# Exibir
numero_de_palavras.show(100)

# Encerrar sessão
spark.stop()
