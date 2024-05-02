#!/bin/bash
echo Começando o processamento das vendas...

# Criando diretório de vendas
# -p : Sem erro se já existir
mkdir -p vendas

# Copiando csv para o diretório de vendas

cp dados_de_vendas.csv ./vendas

# Criando diretório de backup, dentro do diretório vendas

mkdir -p vendas/backup

# Copiando csv com novo nome (dados-yyyymmdd.csv)

cp dados_de_vendas.csv vendas/backup/dados-$(date +"%Y%m%d").csv

# Renomeando arquivo do backup (backup-dados-yyyymmdd.csv)

mv vendas/backup/dados-$(date +"%Y%m%d").csv vendas/backup/backup-dados-$(date +"%Y%m%d").csv

# Salvar o nome do arquivo, para usos futuros
NOME_ARQUIVO="vendas/backup/backup-dados-$(date +'%Y%m%d').csv"

<< comentario
Criando um relatório dentro do diretório de backup, contendo:
- Data e hora atuais (yyyy/mm/dd hh:mm) - $(date +'%Y/%m/%d %H:%M')
- Data do primeiro registro de venda:
- Data do último registro de venda
- Total de itens vendidos 

    tr ',' '\n' (separar cada ocorrência de ',' em uma linha)
    tail -n 1 (manter somente a ultima linha - coluna de data)

comentario

echo -e "Criando relatório..."

# Criando um relatório dentro do diretório de backup
echo -e "$(date +'%Y/%m/%d %H:%M')
$(head -n 2 $NOME_ARQUIVO | tail -1 | tr ',' '\n' | tail -n 1)
$(tail -n 1 $NOME_ARQUIVO | tr ',' '\n' | tail -n 1)
$(($(wc -l < $NOME_ARQUIVO) - 1))
$(head -n 10 $NOME_ARQUIVO)" > vendas/backup/relatorio-$(date +'%Y%m%d').txt

# Comprimindo a planilha de backup 
# -j : Flag junk -> Ignorar os diretórios e comprimir somente arquivos especificados
zip -j vendas/backup/backup-dados-$(date +'%Y%m%d').zip $NOME_ARQUIVO


# Removendo arquivos

rm $NOME_ARQUIVO
rm vendas/dados_de_vendas.csv

