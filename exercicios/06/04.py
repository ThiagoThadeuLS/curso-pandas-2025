# 06.04 - Quem teve mais transações de Streak?

# %%%

import pandas as pd
pd.set_option('display.max_rows', None)
# %%

produtos = pd.read_csv('../data/produtos.csv', sep=';')
produto = produtos[produtos['DescNomeProduto'] == 'Presença Streak']
# %%

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%

transacao_produto = pd.read_csv('../data/transacao_produto.csv', sep=';')
transacao_produto = transacao_produto[transacao_produto['IdProduto'] == '12']
transacao_produto.head()
# %%

resultado = (transacao_produto.merge(right=transacoes,
                         how='left',
                         on='IdTransacao'
)
.merge(right=produto,
       how='left',
       on='IdProduto'
)
.groupby(by=['IdCliente'])['IdTransacao']
.count()
.reset_index()
.sort_values(by='IdTransacao', ascending=False)
)
# %%

resultado.head(1)