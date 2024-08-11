## Desafio Final, parte 3 (Processamento incial dos dados)

Nesta etapa, há a integração das fontes de origem(no caso, CSV e JSON) em uma única camada confiável de dados. Tal integração será feita com Spark, dentro de um ambiente AWS Glue.

Portanto, o objetivo trazer os dados da camada RAW e criar a camada Trusted(confiável).

### Passos necessários

- Criação de um usuário IAM

- Criação de uma função IAM (IAM Role) para acessar o Glue

- Liberar permissões e criar banco de dados no AWS Lake Formation

### Criando Job no AWS Glue

Foram criados 2 Jobs no AWS Glue. Um para extração dos dados do CSV e um para extração dos dados do JSON. As informações estão particionadas, de modo a sempre pegar os valores mais novos.

[1]: ../evidencias/evidencia1_jobs_glue.png
[2]: ../evidencias/evidencia2_s3_pastas_criadas.png
[3]: ../evidencias/evidencia3_json_particionado.png

| Jobs com CSV e JSON (clique para ver a imagem) |
| :--------------------------------------------: |
|        [![Evidências- Imagem 1][1]][1]         |

| Pastas criadas com sucesso no S3 (clique para ver a imagem) |
| :---------------------------------------------------------: |
|               [![Evidências- Imagem 2][2]][2]               |

| Particionamento na criação das pastas com JSON (clique para ver a imagem) |
| :-----------------------------------------------------------------------: |
|                      [![Evidências- Imagem 3][3]][3]                      |
