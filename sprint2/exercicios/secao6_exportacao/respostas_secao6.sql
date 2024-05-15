-- Etapa 1: Query com os 10 livros mais caros

SELECT 
    cod as CodLivro, titulo as Titulo,
    codautor as CodAutor, nomeautor as NomeAutor, valor as Valor,
    codeditora as CodEditora, nomeeditora as NomeEditora
FROM (
    SELECT 
        l.cod, l.titulo, 
        a.codautor, a.nome as nomeautor, l.valor, 
        e.codeditora, e.nome as nomeeditora,
        ROW_NUMBER() OVER (ORDER BY valor DESC) AS top
    FROM livro l
    JOIN autor a ON a.codautor = l.autor
    JOIN editora e ON e.codeditora = l.editora
) AS rank
WHERE top <= 10

-- Etapa 2: 5 editoras com mais livros na biblioteca

SELECT codeditora as CodEditora, nome as NomeEditora, QuantidadeLivros
FROM (
    SELECT *, count(*) as QuantidadeLivros, ROW_NUMBER() OVER (ORDER BY count(*) DESC) AS top
    FROM livro l
    JOIN editora e on l.editora = e.codeditora
    JOIN endereco en on en.codendereco = e.endereco
    GROUP BY e.codeditora
) AS subquery
WHERE top <= 5 
