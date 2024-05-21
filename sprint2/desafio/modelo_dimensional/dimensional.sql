-- Modelo Dimensional

/**
 * Esses modelos são usados em Data Warehouses, para organizar os dados de forma 
 * mais simples e facilitar as consultas, dentro de estruturas chamadas cubos de dados.
 * 
 * Dentro do modelo dimensional, existem os chamados fatos, que são os dados analisados,
 * e a dimensões, que são filtros/perspectivas de análise desses dados.
*/

-- Portanto, separei a construção do meu banco relacional em dimensional da seguinte forma:

-- Fato: Locação de Veículos

CREATE VIEW fato_locacao AS
SELECT 
idLocacao as codigo,
dataHoraLocacao as locacao,
dataHoraEntrega as entrega,
qtdDiaria,
vlrDiaria,
idCliente,
idVendedor,
idCarro
FROM tb_locacao;

-- Dimensões:

-- Tempo: Data e hora da locação e entrega
CREATE VIEW dim_tempo AS 
WITH datas AS (
    SELECT dataHoraLocacao as data FROM tb_locacao 
        UNION 
    SELECT dataHoraEntrega as data FROM tb_locacao
)
SELECT DISTINCT 
data,
YEAR(data) AS ano,
QUARTER(data) AS trimestre,
MONTH(data) AS mes,
DAY(data) AS dia,
HOUR(data) as hora,
MINUTE(data) as minuto
FROM datas;

-- Cliente
CREATE VIEW dim_clientes AS 
SELECT 
idCliente as codigo,
nomeCliente
FROM tb_cliente;

-- Região: Separar as locações pela região dos clientes que a fizeram
CREATE VIEW dim_regioes AS
SELECT 
idCliente,
cidadeCliente as cidade,
estadoCliente as estado,
paisCliente as pais
FROM tb_cliente;

-- Vendedor
CREATE VIEW dim_vendedores AS
SELECT 
idVendedor,
nomeVendedor,  
sexoVendedor, 
estadoVendedor
FROM tb_vendedor;

-- Carros
CREATE VIEW dim_carros AS
SELECT 
idCarro,
kmCarro AS quilometragem,
classiCarro as chassi,
marcaCarro as marca,
modeloCarro as modelo,
anoCarro, 
tipoCombustivel
FROM tb_carro;