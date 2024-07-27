## Desafio Final, parte 2 (ingestão do JSON)

Nesta etapa, começamos a ingestão dos dados. Os arquivos disponibililizados serão armazenados em um bucket S3, através da biblioteca Python 'Boto3', dentro de um container docker.

Para enriquecer os dados coletados na sprint anterior (arquivos CSV), coletaremos informações da API do *The Movie Database (TMDB)*, através da execução de um código Python no ambiente AWS Lambda. 

As informações irão compor um JSON, que será inserido no S3.


### Etapas

- Criar a imagem docker com o comando `docker build -t camada-sprint7 .`

- Executar o container de modo interativo com o comando `docker run -it camada-sprint7 bash`

- Instalar as dependências necessárias dentro da imagem

Comandos:

    bash-4.2# cd ~
    bash-4.2# mkdir layer_dir
    bash-4.2# cd layer_dir/
    bash-4.2# mkdir python
    bash-4.2# cd python/
    bash-4.2# pip3 install requests boto3


- Executar, en outro terminal, `docker cp <id do container>:/root/layer_dir/camada-sprint7 ./` para copiar a imagem.

- Subir a imagem .zip e o arquivo `lambda.py` para o AWS Lambda, realizar o deploy do código e testar sua execução.


