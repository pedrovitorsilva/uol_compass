-- Testes no filme Matrix (id = tt0133093)

select * from "fato_filme" where id = 'tt0133093';

select * from "dim_tempo" where id = 'tt0133093';

-- Consulta para os gêneros
SELECT 
    ff.titulo,
    'Genero' AS nome_campo,
    dg.nome AS valor
FROM 
    fato_filme ff
JOIN 
    bridge_filmes_genero bfg ON ff.id = bfg.id_filme
JOIN 
    dim_genero dg ON bfg.id_genero = dg.id
WHERE 
    ff.id = 'tt0133093'

UNION ALL

-- Consulta para as produtoras
SELECT 
    ff.titulo,
    'Produtora' AS nome_campo,
    dp.nome AS valor
FROM 
    fato_filme ff
JOIN 
    bridge_filmes_produtora bfp ON ff.id = bfp.id_filme
JOIN 
    dim_produtora dp ON bfp.id_produtora = dp.id
WHERE 
    ff.id = 'tt0133093'

UNION ALL

-- Consulta para as palavras-chave
SELECT 
    ff.titulo,
    'Palavra_Chave' AS nome_campo,
    dpk.nome AS valor
FROM 
    fato_filme ff
JOIN 
    bridge_filmes_palavra_chave bfpk ON ff.id = bfpk.id_filme
JOIN 
    dim_palavra_chave dpk ON bfpk.id_palavra_chave = dpk.id
WHERE 
    ff.id = 'tt0133093';
