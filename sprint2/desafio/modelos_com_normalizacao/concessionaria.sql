CREATE database sprint2;
USE sprint2;

CREATE TABLE tb_cliente (
idCliente       INT PRIMARY KEY,
nomeCliente     VARCHAR(100) NOT NULL,
cidadeCliente   VARCHAR(40) NOT NULL,
estadoCliente   VARCHAR(40) NOT NULL,
paisCliente     VARCHAR(40) NOT NULL
);

CREATE TABLE tb_carro (
idCarro         INT PRIMARY KEY,
kmCarro         INT,
classiCarro     VARCHAR(50) NOT NULL,
marcaCarro      VARCHAR(80),
modeloCarro     VARCHAR(80),
anoCarro        INT,
tipoCombustivel VARCHAR(20)
);

CREATE TABLE tb_vendedor (
idVendedor      INT PRIMARY KEY,
nomeVendedor    VARCHAR(15) NOT NULL,
sexoVendedor    SMALLINT,
estadoVendedor  VARCHAR(40)
);

CREATE TABLE tb_locacao (
idLocacao       INT PRIMARY KEY,
dataHoraLocacao DATETIME NOT NULL,
dataHoraEntrega DATETIME,
qtdDiaria       INT NOT NULL,
vlrDiaria       DECIMAL(18,2) NOT NULL,
-- Chaves Estrangeiras 
idCliente       INT,
idVendedor      INT,
idCarro         INT,
FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro)
);
