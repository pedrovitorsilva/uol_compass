-- SQLite
-- Questão 8 #############################################################

WITH subquery AS (
    SELECT b.cdvdd, b.nmvdd, count(*) as numero_vendas
    FROM tbvendas a
    JOIN tbvendedor b on a.cdvdd = b.cdvdd
    WHERE status = 'Concluído'
    GROUP BY b.cdvdd
)
SELECT cdvdd, nmvdd
FROM subquery
WHERE numero_vendas = (SELECT MAX(numero_vendas) FROM subquery);

-- Questão 9 #############################################################

-- Com With

WITH ProductSales AS (
    SELECT cdpro, nmpro, COUNT(*) as quantidade
    FROM tbvendas
    WHERE status = 'Concluído'
        AND dtven > '2014-02-03' AND dtven < '2018-02-02'
    GROUP BY cdpro, nmpro
)
SELECT cdpro, nmpro
FROM ProductSales
WHERE quantidade = (
    SELECT MAX(quantidade)
    FROM ProductSales
);

-- Sem With
-- SELECT cdpro, nmpro
-- FROM tbvendas
-- WHERE status = 'Concluído'
-- AND dtven > '2014-02-03' AND dtven < '2018-02-02'
-- GROUP BY cdpro
-- HAVING count(*) = (
--     SELECT MAX(quantidade) 
--     FROM (
--         SELECT cdpro, nmpro, count(*) as quantidade 
--         FROM tbvendas
--         WHERE status = 'Concluído'
--         AND dtven > '2014-02-03' AND dtven < '2018-02-02'
--         GROUP BY cdpro
--     )
-- )


-- Questão 10 #############################################################

-- Uso do With apenas para facilitar a formatação e legibilidade
-- Poucos ajustes podem remover o with do código a seguir

WITH subquery AS (
    SELECT 
        a.nmvdd as vendedor, 
        SUM((b.qtd * b.vrunt)) as valor_total_vendas, 
        a.perccomissao
    FROM tbvendedor a
    LEFT JOIN tbvendas b on a.cdvdd = b.cdvdd 
    WHERE b.status = 'Concluído'
    GROUP BY a.cdvdd
)
SELECT 
    vendedor, 
    valor_total_vendas, 
    ROUND(valor_total_vendas * subquery.perccomissao / 100, 2) as comissao
FROM 
    subquery
ORDER BY comissao DESC;

-- Questão 11 #############################################################
WITH subquery as (
    SELECT cdcli, nmcli, SUM(v.qtd * v.vrunt) as gasto
    FROM tbvendas v
    GROUP BY cdcli
)
SELECT cdcli, nmcli, gasto
FROM subquery
WHERE gasto = (SELECT MAX(gasto) FROM subquery);

-- Questão 12 #############################################################

WITH subquery AS (
    SELECT 
        a.cdvdd,
        SUM((b.qtd * b.vrunt)) as valor_total_vendas
    FROM tbvendedor a
    JOIN tbvendas b on a.cdvdd = b.cdvdd 
    WHERE b.status = 'Concluído'
    GROUP BY a.cdvdd
)
SELECT d.cddep, d.nmdep, d.dtnasc, valor_total_vendas 
FROM subquery c
JOIN tbdependente d ON d.cdvdd = c.cdvdd 
WHERE valor_total_vendas = (SELECT MIN(valor_total_vendas) FROM subquery);

-- Questão 13 #############################################################
SELECT cdpro, nmcanalvendas, nmpro, quantidade_vendas
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (ORDER BY quantidade_vendas ASC) AS top
    FROM (
        SELECT cdpro, nmcanalvendas, nmpro, SUM(qtd) AS quantidade_vendas
        FROM tbvendas
        WHERE status = 'Concluído'
        GROUP BY cdpro, nmcanalvendas
    ) AS subquery1
) AS subquery2
WHERE top <= 10;


-- Questão 14 #############################################################

SELECT estado, ROUND(AVG(qtd * vrunt),2) as gastomedio 
FROM tbvendas 
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio DESC;

-- Questão 15 #############################################################

SELECT cdven
FROM tbvendas
WHERE deletado;

--  Se o campo for numérico, ele tratará qualquer valor diferente de zero como verdadeiro 
--  e zero como falso.

--  Se o campo for uma string, ele tratará qualquer string não vazia como verdadeiro 
-- e a string vazia como falso.

-- Questão 16 #############################################################

SELECT estado, nmpro, ROUND(AVG(qtd),4) as quantidade_media
FROM tbvendas a
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro;