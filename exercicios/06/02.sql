-- 06.02 - Quais são os usuários que mais fizeram transações? 
-- Considere os 10 primeiros.

SELECT 
    c.idCliente,
    count(IdTransacao) AS qtdeTransacoes

FROM clientes AS c

LEFT JOIN transacoes AS t
ON c.idCliente = t.IdCliente

GROUP BY 1
ORDER BY 2 DESC

LIMIT 10


