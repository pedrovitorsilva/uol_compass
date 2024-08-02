import contextlib
import random
import io
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql.functions import udf, col
from tabulate import tabulate

# UDF = User Defined Functions


def definir_escolaridade():
    return random.choice(["Fundamental", "Médio", "Superior"])


def definir_pais():
    return random.choice(["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia",
                          "Equador", "Guiana", "Paraguai", "Peru", "Suriname",
                          "Uruguai", "Venezuela"])


def definir_ano():
    return random.randint(1945, 2010)


def imprimir(df, linhas=10):
    '''Exibe os dados e salva a tabela.'''

    # Exibir
    df.show(linhas)

    # Salvar

    data = df.limit(linhas).collect()
    headers = [header.capitalize() for header in df.columns]

    # Formatar Headers
    headers = list(map(lambda x: x.replace('Anonascimento', 'Ano de Nascimento').replace(
        'Geracao', 'Geração').replace('Pais', 'País'), headers))

    markdown = tabulate(data, headers=headers,
                              tablefmt="pipe", stralign="center")

    return "\n" + markdown + "\n"


# Inicializa Spark
spark = SparkSession.builder.appName("Exercicio Spark").getOrCreate()

# Tentar exibir menos logs no terminal, tornando a impressão mais "limpa"
# Imprimir apenas logs e erros no terminal
spark.sparkContext.setLogLevel("ERROR")

df_nomes = spark.read.csv("nomes_aleatorios.txt", sep=",",
                          inferSchema=True, header=False).toDF("nomes")

# PERSISTIR O DATAFRAME
df_nomes = df_nomes.cache()

# Lista para armazenar as saídas
prints = []

# Etapa 1 e 2: Mostrar nomes
prints.append("## Mostrar nomes iniciais\n" + imprimir(df_nomes))

# Etapa 3: Adicionar coluna escolaridade
random_escolaridade_udf = udf(definir_escolaridade, StringType())
df_nomes = df_nomes.withColumn("escolaridade", random_escolaridade_udf())
df_nomes = df_nomes.cache()

prints.append("## Adicionar coluna 'Escolaridade'\n" + imprimir(df_nomes))

# Etapa 4: Adicionar coluna pais
random_paises_udf = udf(definir_pais, StringType())
df_nomes = df_nomes.withColumn("pais", random_paises_udf())
df_nomes = df_nomes.cache()

prints.append("## Adicionar coluna 'País'\n" + imprimir(df_nomes))

# Etapa 5: Adicionar coluna anoNascimento
random_ano_udf = udf(definir_ano, IntegerType())
df_nomes = df_nomes.withColumn("anoNascimento", random_ano_udf())
df_nomes = df_nomes.cache()

prints.append("## Adicionar coluna 'Ano de Nascimento'\n" + imprimir(df_nomes))

# Etapa 6: Filtro por ano ( > 2000 ) com Select
df_select = df_nomes.select('*').where(col("anoNascimento") > 2000)

prints.append("## Filtro por ano ( > 2000 ) com Select\n" +
              imprimir(df_select))

# Etapa 7: Filtro por ano ( > 2000 ) com SQL
df_nomes.createOrReplaceTempView("pessoas")

prints.append("## Filtro por ano ( > 2000 ) com SQL\n" + imprimir(
    spark.sql("SELECT * FROM pessoas WHERE anoNascimento > 2000 LIMIT 10")))

# Etapa 8: Filtro por ano (entre 1980 e 1994) com Select
df_select = df_nomes.select(
    '*').where("anoNascimento >= 1980 AND anoNascimento <= 1994")

prints.append(
    "## Filtro por ano (entre 1980 e 1994) com Select\n" + imprimir(df_select))

# Etapa 9: Filtro por ano (entre 1980 e 1994) com SQL
prints.append("## Filtro por ano (entre 1980 e 1994) com SQL\n" + imprimir(
    spark.sql("SELECT * FROM pessoas WHERE anoNascimento BETWEEN 1980 AND 1994 LIMIT 10")))

# Etapa 10: Agrupar por geração e país
df_resultado = spark.sql(''' 
SELECT
    CASE
        WHEN anoNascimento IS NULL THEN 'Desconhecida'
        WHEN anoNascimento > 1944 AND anoNascimento < 1964 THEN 'Baby Boomers'
        WHEN anoNascimento < 1979 THEN 'Geração X'
        WHEN anoNascimento < 1995 THEN 'Geração Y'
        ELSE 'Geração Z'
    END as geracao,
    pais,
    COUNT(*) as quantidade
FROM pessoas
GROUP BY geracao, pais
ORDER BY pais, geracao
''')

prints.append("## Agrupar por geração e país\n" +
              imprimir(df_resultado, linhas=100))

# Salvar todas as saídas em um arquivo Markdown
with open("resultados.md", "w") as file:
    file.write("\n\n".join(prints))

# Encerrar Spark
spark.stop()
