# Etapas de execução:

### Instalar imagem, se não já estiver instalada:
`docker pull jupyter/all-spark-notebook`

### Executar os comandos:

`docker run -p 8000:8888 -it jupyter/all-spark-notebook:latest`

### Abrir outro terminal e executar os comandos:

`docker ps` &rarr; Anotar {ID} do container

`docker rename {ID} jupyter`

`docker exec -it jupyter pyspark`

### Testar:

Dentro do Jupyter Notebook, executar `contador.py`.

Outra opção é testar com spark-submit `contador .py`.
