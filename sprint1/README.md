# Sprint 1 - Ecommerce

O objetivo da sprint era exercitar os comandos Linux aprendidos, através da criação de um arquivo, realizando os comandos de forma automática.

## Realização do Desafio

Os comandos foram executados dentro do diretório ./sprint1/desafio/ecommmere

### Arquivo de Processamento:

Para permitir a execução do script, execute o seguinte comando:

`chmod 777 ./processamento_de_vendas.sh` 

**Código pode ser executado com o comando:**

` ./processamento_de_vendas.sh `  

OU

` sh processamento_de_vendas.sh `

### Agendamento da Execução:

A execução pode ser agendada com o comando **`crontab -e`.**

Ao final do arquivo, adicione a seguinte linha:

`27 15 * * 1-4 cd home/seu/endereco/do/arquivo ** ./processamento_de_vendas.sh > /dev/pts/0`


Para permitir a execução do script, execute o seguinte comando:

`chmod 777 processamento_de_vendas.sh` 

### Simular Relatórios:

Para simular os relatórios, agendei a execução com o comando acima. Em seguida, optei por mudar a data e horário do meu computador.

Após criados pelo menos 3 relatórios, pode-se executar o passo abaixo.

### Consolidar Processamento:

Para permitir a execução do script, execute o seguinte comando:

`chmod 777 consolidador_de_processamento_de_vendas.sh` 

**O relatório final (relatorio_fina.txt) pode ser criado com os comandos:**

` ./consolidador_de_processamento_de_vendas.sh ` 

OU 

` sh consolidador_de_processamento_de_vendas.sh `