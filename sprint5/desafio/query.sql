WITH ConsumoMedio AS (
    SELECT 
        Local,
        Identificador,
        AVG(CAST(Consumo AS FLOAT)) AS MediaConsumo,
        MAX(CAST(Consumo AS FLOAT)) AS MaiorConsumo,
        CASE WHEN Consumo = MAX(Consumo) OVER (PARTITION BY Local, Identificador) THEN Mês END AS MesMaiorConsumo
    FROM df
    GROUP BY Local, Identificador
)
SELECT 
    Local,
    MediaConsumo as 'Média de Consumo (em m³)',
    CASE 
        WHEN MediaConsumo < 100.0 THEN 'Baixo'
        WHEN 100.0 < MediaConsumo AND MediaConsumo < 1000.0 THEN 'Médio'
        ELSE 'Alto'
    END AS 'Perfil de Consumo',
    STRFTIME('%m/%Y', MesMaiorConsumo) AS 'Mès de Maior Consumo',
    MaiorConsumo AS 'Maior Consumo (em m³)'
FROM ConsumoMedio
WHERE LOWER(Local) NOT LIKE '%alvorada%'
