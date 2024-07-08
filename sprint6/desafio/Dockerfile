FROM python

WORKDIR /sprint6

COPY . .

## Instalando bibliotecas
RUN pip install -r requirements.txt 

## Descompactando arquivos e removendo cópias
RUN apt-get update && apt-get install -y unzip

RUN unzip Filmes_e_Series.zip && rm Filmes_e_Series.zip

CMD ["python", "ingestao.py" ]