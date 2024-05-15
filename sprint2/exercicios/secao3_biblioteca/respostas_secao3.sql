-- SQLite
-- Questão 1 #############################################################

SELECT *
FROM livro 
WHERE CAST(strftime('%Y', publicacao) AS INTEGER) > 2014
ORDER BY cod;

-- Questão 2 #############################################################

SELECT titulo,valor
FROM (
    SELECT titulo, valor,
        ROW_NUMBER() OVER (ORDER BY valor DESC) AS top
    FROM livro
) AS rank
WHERE top <= 10;

-- Questão 3 #############################################################

SELECT quantidade, nome, estado, cidade
FROM (
    SELECT *, count(*) as quantidade, ROW_NUMBER() OVER (ORDER BY count(*) DESC) AS top
    FROM livro l
    JOIN editora e on l.editora = e.codeditora
    JOIN endereco en on en.codendereco = e.endereco
    GROUP BY e.codeditora
) AS subquery
WHERE top <= 5;


-- Questão 4 #############################################################

SELECT nome,codautor, nascimento, count(l.cod) as quantidade -- Não contar linhas de autores com livros nulos
FROM autor a
LEFT JOIN livro l ON a.codautor = l.autor -- Autores sem livros: left join
GROUP BY a.codautor
ORDER BY a.nome;

-- Questão 5 #############################################################

SELECT DISTINCT(a.nome)
FROM autor a
JOIN livro l ON a.codautor = l.autor 
JOIN editora e on l.editora = e.codeditora
JOIN endereco en on en.codendereco = e.endereco
WHERE en.estado NOT IN ('RIO GRANDE DO SUL', 'PARANÁ', 'SANTA CATARINA')
ORDER BY a.nome;

-- Questão 6 #############################################################

-- Com With

WITH quantidade_livros AS (
    SELECT a.codautor, a.nome, COUNT(l.cod) as quantidade_publicacoes
    FROM autor a
    LEFT JOIN livro l ON a.codautor = l.autor 
    GROUP BY a.codautor
)
SELECT *
FROM quantidade_livros 
WHERE quantidade_publicacoes = (
    SELECT MAX(quantidade_publicacoes) 
    FROM quantidade_livros
);


-- Sem With

-- SELECT codautor, nome, count(l.cod) as quantidade_publicacoes
-- FROM autor a
-- LEFT JOIN livro l ON a.codautor = l.autor -- Autores sem livros: left join
-- GROUP BY a.codautor
-- HAVING quantidade_publicacoes = (
--     SELECT MAX(quantidade)
--     FROM (
--         SELECT a.nome, COUNT(*) as quantidade
--         FROM autor a
--         LEFT JOIN livro l ON a.codautor = l.autor 
--         GROUP BY a.codautor) 
-- )



-- Questão 7 #############################################################

SELECT nome
FROM autor a
LEFT JOIN livro l ON a.codautor = l.autor
WHERE l.autor IS NULL;