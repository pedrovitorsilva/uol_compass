## Mostrar nomes iniciais

|       Nomes       |
|:-----------------:|
|  Frances Bennet   |
|   Jamie Russell   |
|  Edward Kistler   |
|   Sheila Maurer   |
| Donald Golightly  |
|    David Gray     |
|    Joy Bennett    |
|    Paul Kriese    |
| Berniece Ornellas |
|   Brian Farrell   |


## Adicionar coluna 'Escolaridade'

|       Nomes       |  Escolaridade  |
|:-----------------:|:--------------:|
|  Frances Bennet   |    Superior    |
|   Jamie Russell   |     Médio      |
|  Edward Kistler   |     Médio      |
|   Sheila Maurer   |  Fundamental   |
| Donald Golightly  |    Superior    |
|    David Gray     |    Superior    |
|    Joy Bennett    |  Fundamental   |
|    Paul Kriese    |    Superior    |
| Berniece Ornellas |     Médio      |
|   Brian Farrell   |     Médio      |


## Adicionar coluna 'País'

|       Nomes       |  Escolaridade  |   País    |
|:-----------------:|:--------------:|:---------:|
|  Frances Bennet   |    Superior    |   Peru    |
|   Jamie Russell   |     Médio      |  Equador  |
|  Edward Kistler   |     Médio      |  Brasil   |
|   Sheila Maurer   |  Fundamental   | Argentina |
| Donald Golightly  |    Superior    |  Guiana   |
|    David Gray     |    Superior    |   Chile   |
|    Joy Bennett    |  Fundamental   |   Peru    |
|    Paul Kriese    |    Superior    |  Equador  |
| Berniece Ornellas |     Médio      | Venezuela |
|   Brian Farrell   |     Médio      |  Brasil   |


## Adicionar coluna 'Ano de Nascimento'

|       Nomes       |  Escolaridade  |   País    |   Ano de Nascimento |
|:-----------------:|:--------------:|:---------:|--------------------:|
|  Frances Bennet   |    Superior    |   Peru    |                1977 |
|   Jamie Russell   |     Médio      |  Equador  |                1992 |
|  Edward Kistler   |     Médio      |  Brasil   |                2007 |
|   Sheila Maurer   |  Fundamental   | Argentina |                1966 |
| Donald Golightly  |    Superior    |  Guiana   |                1967 |
|    David Gray     |    Superior    |   Chile   |                1985 |
|    Joy Bennett    |  Fundamental   |   Peru    |                1978 |
|    Paul Kriese    |    Superior    |  Equador  |                1984 |
| Berniece Ornellas |     Médio      | Venezuela |                1968 |
|   Brian Farrell   |     Médio      |  Brasil   |                1946 |


## Filtro por ano ( > 2000 ) com Select

|      Nomes       |  Escolaridade  |   País    |   Ano de Nascimento |
|:----------------:|:--------------:|:---------:|--------------------:|
|  Edward Kistler  |     Médio      |  Brasil   |                2007 |
|   Leroy Strahl   |    Superior    | Colômbia  |                2005 |
|   Albert Leef    |  Fundamental   | Suriname  |                2008 |
|   Rebecca Snow   |     Médio      |   Peru    |                2001 |
|  Wilfredo Grant  |     Médio      |   Peru    |                2009 |
|   Lisa Baxley    |     Médio      |  Equador  |                2001 |
|  Ashley Trosper  |    Superior    | Argentina |                2001 |
| Cristina Sheston |     Médio      | Suriname  |                2009 |
|   Hugo Dayton    |    Superior    | Venezuela |                2005 |
|   Rita Walter    |    Superior    | Venezuela |                2004 |


## Filtro por ano ( > 2000 ) com SQL

|      Nomes       |  Escolaridade  |   País    |   Ano de Nascimento |
|:----------------:|:--------------:|:---------:|--------------------:|
|  Edward Kistler  |     Médio      |  Brasil   |                2007 |
|   Leroy Strahl   |    Superior    | Colômbia  |                2005 |
|   Albert Leef    |  Fundamental   | Suriname  |                2008 |
|   Rebecca Snow   |     Médio      |   Peru    |                2001 |
|  Wilfredo Grant  |     Médio      |   Peru    |                2009 |
|   Lisa Baxley    |     Médio      |  Equador  |                2001 |
|  Ashley Trosper  |    Superior    | Argentina |                2001 |
| Cristina Sheston |     Médio      | Suriname  |                2009 |
|   Hugo Dayton    |    Superior    | Venezuela |                2005 |
|   Rita Walter    |    Superior    | Venezuela |                2004 |


## Filtro por ano (entre 1980 e 1994) com Select

|      Nomes       |  Escolaridade  |   País   |   Ano de Nascimento |
|:----------------:|:--------------:|:--------:|--------------------:|
|  Jamie Russell   |     Médio      | Equador  |                1992 |
|    David Gray    |    Superior    |  Chile   |                1985 |
|   Paul Kriese    |    Superior    | Equador  |                1984 |
|  Herbert Morris  |  Fundamental   | Suriname |                1983 |
|     Lois Ly      |     Médio      |  Guiana  |                1982 |
|   Frank Wiley    |  Fundamental   | Suriname |                1989 |
| Wallace Mitchell |    Superior    |  Guiana  |                1991 |
|   Jessie Jean    |     Médio      | Suriname |                1985 |
|    John Meyer    |     Médio      | Bolívia  |                1991 |
|    Ned Tester    |  Fundamental   | Uruguai  |                1990 |


## Filtro por ano (entre 1980 e 1994) com SQL

|      Nomes       |  Escolaridade  |   País   |   Ano de Nascimento |
|:----------------:|:--------------:|:--------:|--------------------:|
|  Jamie Russell   |     Médio      | Equador  |                1992 |
|    David Gray    |    Superior    |  Chile   |                1985 |
|   Paul Kriese    |    Superior    | Equador  |                1984 |
|  Herbert Morris  |  Fundamental   | Suriname |                1983 |
|     Lois Ly      |     Médio      |  Guiana  |                1982 |
|   Frank Wiley    |  Fundamental   | Suriname |                1989 |
| Wallace Mitchell |    Superior    |  Guiana  |                1991 |
|   Jessie Jean    |     Médio      | Suriname |                1985 |
|    John Meyer    |     Médio      | Bolívia  |                1991 |
|    Ned Tester    |  Fundamental   | Uruguai  |                1990 |


## Agrupar por geração e país

|   Geração    |   País    |   Quantidade |
|:------------:|:---------:|-------------:|
| Baby Boomers | Argentina |       239517 |
|  Geração X   | Argentina |       189685 |
|  Geração Y   | Argentina |       201651 |
|  Geração Z   | Argentina |       201360 |
| Baby Boomers |  Bolívia  |       239409 |
|  Geração X   |  Bolívia  |       189345 |
|  Geração Y   |  Bolívia  |       201934 |
|  Geração Z   |  Bolívia  |       202385 |
| Baby Boomers |  Brasil   |       239542 |
|  Geração X   |  Brasil   |       188889 |
|  Geração Y   |  Brasil   |       201861 |
|  Geração Z   |  Brasil   |       202101 |
| Baby Boomers |   Chile   |       240001 |
|  Geração X   |   Chile   |       189329 |
|  Geração Y   |   Chile   |       201852 |
|  Geração Z   |   Chile   |       201862 |
| Baby Boomers | Colômbia  |       240229 |
|  Geração X   | Colômbia  |       189664 |
|  Geração Y   | Colômbia  |       201778 |
|  Geração Z   | Colômbia  |       202081 |
| Baby Boomers |  Equador  |       239590 |
|  Geração X   |  Equador  |       189760 |
|  Geração Y   |  Equador  |       202090 |
|  Geração Z   |  Equador  |       201470 |
| Baby Boomers |  Guiana   |       240355 |
|  Geração X   |  Guiana   |       188739 |
|  Geração Y   |  Guiana   |       202943 |
|  Geração Z   |  Guiana   |       201634 |
| Baby Boomers | Paraguai  |       239762 |
|  Geração X   | Paraguai  |       188703 |
|  Geração Y   | Paraguai  |       202307 |
|  Geração Z   | Paraguai  |       202328 |
| Baby Boomers |   Peru    |       239896 |
|  Geração X   |   Peru    |       189110 |
|  Geração Y   |   Peru    |       202679 |
|  Geração Z   |   Peru    |       202182 |
| Baby Boomers | Suriname  |       240665 |
|  Geração X   | Suriname  |       188795 |
|  Geração Y   | Suriname  |       202424 |
|  Geração Z   | Suriname  |       202634 |
| Baby Boomers |  Uruguai  |       239540 |
|  Geração X   |  Uruguai  |       189558 |
|  Geração Y   |  Uruguai  |       202322 |
|  Geração Z   |  Uruguai  |       202181 |
| Baby Boomers | Venezuela |       240065 |
|  Geração X   | Venezuela |       189323 |
|  Geração Y   | Venezuela |       202045 |
|  Geração Z   | Venezuela |       202427 |
