# Sprint 6 - AWS

O objetivo dessa sprint foi apresentar os diferentes recursos disponibilizados pela AWS, e exercitar os conteúdos aprendidos.

## Certificados

No diretório `sprint6/certificados` estão os certificados da AWS referentes a essa sprint.

## Desafio

O desafio desta sprint envolveu o início do desafio final do programa de bolsas da Uol Compass. Aqui começamos a criação de um data lake através da ingestão de dados.

## Desafio Final, parte 1
Nesta etapa, começamos a ingestão dos dados. Os arquivos disponibililizados serão armazenados em um bucket S3, através da biblioteca Python 'Boto3', dentro de um container docker. 

## Tema

O tema que planejo abordar é de "**Filmes de Ficção Científica nas décadas de 80 e 90 (1980 - 1999)**".

Perguntas que planejo responder:

- Quais os filmes melhor avaliados?
- Quais outros gêneros mais aparecem junto com esse tipo de filme?

### Etapas

#### Abrir o diretorio `./sprint6/desafio/` e executar os seguintes comandos:

- Criar a imagem docker com o comando `docker build -t ingestao-sprint6 .`

- Executar o container de modo interativo com o comando `docker run -it ingestao-sprint6`

## Evidências

![](evidencias/imagem1.png)
