SELECT 
    c.idCliente,
    sum(t.QtdePontos) AS SumPontosDebitados

FROM clientes AS c

LEFT JOIN transacoes AS t
ON c.idCliente = t.IdCliente

WHERE t.QtdePontos > 0

GROUP BY 1
ORDER BY 2 DESC

LIMIT 1

