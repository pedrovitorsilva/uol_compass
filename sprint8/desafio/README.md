## Desafio Final, parte 3 (Processamento incial dos dados)

Nesta etapa, há a integração das fontes de origem(no caso, CSV e JSON) em uma única camada confiável de dados. Tal integração será feita com Spark, dentro de um ambiente AWS Glue.

### Passos necessários

- Criação de um usuário IAM

- Criação de uma função IAM (IAM Role) para acessar o Glue

- Liberar permissões e criar banco de dados no AWS Lake Formation

### Criando Job no AWS Glue

Foram criados 2 Jobs no AWS Glue. Um para extração dos dados do CSV e um para extração dos dados do JSON, ambos em formato RAW dentro do S3.
