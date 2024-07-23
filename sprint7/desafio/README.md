mudanças(otimização) nas perguntas

O desafio desta sprint envolveu o início do desafio final do programa de bolsas da Uol Compass.

O tema que planejo abordar é de "**Filmes de Ficção Científica mais populares nas décadas de 80 e 90 (1980 - 1999)**".

Perguntas que planejo responder:

- Quais os filmes melhor avaliados, ordenados por popularidade?
- Quais outros gêneros mais aparecem junto com esse tipo de filme? E quais as palavras-chave mais comuns?


## Desafio Final, parte 1

Nesta etapa, começamos a ingestão dos dados. Os arquivos disponibililizados serão armazenados em um bucket S3, através da biblioteca Python 'Boto3', dentro de um container docker.

### Etapas

#### Abrir o diretorio `./sprint6/desafio/` e executar os seguintes comandos:

- Criar a imagem docker com o comando `docker build -t ingestao-sprint6 .`

- Executar o container de modo interativo com o comando `docker run -it ingestao-sprint6`

## Evidências

<details>

<summary> Clique Aqui 🔗</summary>
<br/>

|                   Bucket S3 Vazio                   |
| :-------------------------------------------------: |
|         ![S3 vazio](evidencias/imagem1.png)         |
|                Execução do Container                |
|  ![Execução do container](evidencias/imagem2.png)   |
|            Bucket S3, Agora com Conteúdo            |
| ![S3 agora possui conteúdo](evidencias/imagem3.png) |

</details>
