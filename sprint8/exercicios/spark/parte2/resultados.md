# Mostrar nomes iniciais
+-----------------+
|nomes            |
+-----------------+
|Frances Bennet   |
|Jamie Russell    |
|Edward Kistler   |
|Sheila Maurer    |
|Donald Golightly |
|David Gray       |
|Joy Bennett      |
|Paul Kriese      |
|Berniece Ornellas|
|Brian Farrell    |
+-----------------+
only showing top 10 rows



# Adicionar coluna escolaridade
+-----------------+------------+
|nomes            |escolaridade|
+-----------------+------------+
|Frances Bennet   |Fundamental |
|Jamie Russell    |Fundamental |
|Edward Kistler   |Médio       |
|Sheila Maurer    |Superior    |
|Donald Golightly |Superior    |
|David Gray       |Fundamental |
|Joy Bennett      |Médio       |
|Paul Kriese      |Superior    |
|Berniece Ornellas|Médio       |
|Brian Farrell    |Superior    |
+-----------------+------------+
only showing top 10 rows



# Adicionar coluna pais
+-----------------+------------+---------+
|nomes            |escolaridade|pais     |
+-----------------+------------+---------+
|Frances Bennet   |Fundamental |Argentina|
|Jamie Russell    |Superior    |Chile    |
|Edward Kistler   |Fundamental |Suriname |
|Sheila Maurer    |Fundamental |Chile    |
|Donald Golightly |Fundamental |Guiana   |
|David Gray       |Superior    |Uruguai  |
|Joy Bennett      |Superior    |Chile    |
|Paul Kriese      |Superior    |Brasil   |
|Berniece Ornellas|Médio       |Colômbia |
|Brian Farrell    |Médio       |Peru     |
+-----------------+------------+---------+
only showing top 10 rows



# Adicionar coluna anoNascimento
+-----------------+------------+---------+-------------+
|nomes            |escolaridade|pais     |anoNascimento|
+-----------------+------------+---------+-------------+
|Frances Bennet   |Fundamental |Suriname |1945         |
|Jamie Russell    |Superior    |Bolívia  |1982         |
|Edward Kistler   |Superior    |Suriname |1971         |
|Sheila Maurer    |Médio       |Brasil   |2001         |
|Donald Golightly |Superior    |Argentina|2001         |
|David Gray       |Superior    |Bolívia  |1990         |
|Joy Bennett      |Superior    |Venezuela|1993         |
|Paul Kriese      |Superior    |Brasil   |1946         |
|Berniece Ornellas|Médio       |Guiana   |1948         |
|Brian Farrell    |Médio       |Uruguai  |1973         |
+-----------------+------------+---------+-------------+
only showing top 10 rows



# Filtro por ano ( > 2000 ) com Select
+--------------+------------+---------+-------------+
|nomes         |escolaridade|pais     |anoNascimento|
+--------------+------------+---------+-------------+
|Frances Bennet|Médio       |Suriname |2009         |
|Jamie Russell |Fundamental |Venezuela|2009         |
|Brian Farrell |Superior    |Bolívia  |2007         |
|Ernest Hulet  |Fundamental |Brasil   |2003         |
|David Medina  |Médio       |Venezuela|2008         |
|Albert Leef   |Médio       |Uruguai  |2003         |
|Wilfredo Grant|Fundamental |Bolívia  |2002         |
|Donald Vogt   |Superior    |Chile    |2008         |
|Milton Dillon |Médio       |Paraguai |2007         |
|Ashley Trosper|Médio       |Brasil   |2007         |
+--------------+------------+---------+-------------+
only showing top 10 rows



# Filtro por ano ( > 2000 ) com SQL
+--------------+------------+---------+-------------+
|nomes         |escolaridade|pais     |anoNascimento|
+--------------+------------+---------+-------------+
|Frances Bennet|Médio       |Suriname |2009         |
|Jamie Russell |Fundamental |Venezuela|2009         |
|Brian Farrell |Superior    |Bolívia  |2007         |
|Ernest Hulet  |Fundamental |Brasil   |2003         |
|David Medina  |Médio       |Venezuela|2008         |
|Albert Leef   |Médio       |Uruguai  |2003         |
|Wilfredo Grant|Fundamental |Bolívia  |2002         |
|Donald Vogt   |Superior    |Chile    |2008         |
|Milton Dillon |Médio       |Paraguai |2007         |
|Ashley Trosper|Médio       |Brasil   |2007         |
+--------------+------------+---------+-------------+



# Filtro por ano (entre 1980 e 1994) com Select
+-----------------+------------+---------+-------------+
|nomes            |escolaridade|pais     |anoNascimento|
+-----------------+------------+---------+-------------+
|Edward Kistler   |Médio       |Uruguai  |1991         |
|Berniece Ornellas|Médio       |Colômbia |1981         |
|Lorenzo Woodis   |Médio       |Paraguai |1986         |
|Helen Blackwell  |Superior    |Venezuela|1980         |
|Rebecca Snow     |Médio       |Uruguai  |1980         |
|Daryl Page       |Fundamental |Equador  |1982         |
|Kenneth Rayburn  |Médio       |Chile    |1985         |
|Anita Ross       |Superior    |Argentina|1983         |
|John Meyer       |Fundamental |Chile    |1990         |
|Sandra Todd      |Fundamental |Suriname |1987         |
+-----------------+------------+---------+-------------+
only showing top 10 rows



# Filtro por ano (entre 1980 e 1994) com SQL
+-----------------+------------+---------+-------------+
|nomes            |escolaridade|pais     |anoNascimento|
+-----------------+------------+---------+-------------+
|Edward Kistler   |Médio       |Uruguai  |1991         |
|Berniece Ornellas|Médio       |Colômbia |1981         |
|Lorenzo Woodis   |Médio       |Paraguai |1986         |
|Helen Blackwell  |Superior    |Venezuela|1980         |
|Rebecca Snow     |Médio       |Uruguai  |1980         |
|Daryl Page       |Fundamental |Equador  |1982         |
|Kenneth Rayburn  |Médio       |Chile    |1985         |
|Anita Ross       |Superior    |Argentina|1983         |
|John Meyer       |Fundamental |Chile    |1990         |
|Sandra Todd      |Fundamental |Suriname |1987         |
+-----------------+------------+---------+-------------+



# Agrupar por geração e país
+------------+---------+----------+
|geracao     |pais     |quantidade|
+------------+---------+----------+
|Baby Boomers|Argentina|239919    |
|Geração X   |Argentina|189665    |
|Geração Y   |Argentina|201850    |
|Geração Z   |Argentina|202137    |
|Baby Boomers|Bolívia  |239153    |
|Geração X   |Bolívia  |188781    |
|Geração Y   |Bolívia  |202076    |
|Geração Z   |Bolívia  |201935    |
|Baby Boomers|Brasil   |239136    |
|Geração X   |Brasil   |189430    |
|Geração Y   |Brasil   |202320    |
|Geração Z   |Brasil   |201936    |
|Baby Boomers|Chile    |240083    |
|Geração X   |Chile    |188958    |
|Geração Y   |Chile    |201187    |
|Geração Z   |Chile    |202033    |
|Baby Boomers|Colômbia |239794    |
|Geração X   |Colômbia |189833    |
|Geração Y   |Colômbia |201717    |
|Geração Z   |Colômbia |202655    |
|Baby Boomers|Equador  |238964    |
|Geração X   |Equador  |188969    |
|Geração Y   |Equador  |201959    |
|Geração Z   |Equador  |202963    |
|Baby Boomers|Guiana   |240532    |
|Geração X   |Guiana   |189542    |
|Geração Y   |Guiana   |202031    |
|Geração Z   |Guiana   |202815    |
|Baby Boomers|Paraguai |240330    |
|Geração X   |Paraguai |190097    |
|Geração Y   |Paraguai |201296    |
|Geração Z   |Paraguai |201362    |
|Baby Boomers|Peru     |240435    |
|Geração X   |Peru     |189242    |
|Geração Y   |Peru     |202849    |
|Geração Z   |Peru     |201776    |
|Baby Boomers|Suriname |240188    |
|Geração X   |Suriname |189884    |
|Geração Y   |Suriname |202068    |
|Geração Z   |Suriname |202070    |
|Baby Boomers|Uruguai  |239799    |
|Geração X   |Uruguai  |188568    |
|Geração Y   |Uruguai  |202843    |
|Geração Z   |Uruguai  |202189    |
|Baby Boomers|Venezuela|239661    |
|Geração X   |Venezuela|189202    |
|Geração Y   |Venezuela|202679    |
|Geração Z   |Venezuela|201091    |
+------------+---------+----------+

