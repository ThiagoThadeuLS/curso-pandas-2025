# %%

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%

transacoes.groupby(by=['IdCliente']).count()
# %%

transacoes.groupby(by=['IdCliente'], as_index=False)[['IdTransacao']].count()
# %%

sumary = transacoes.groupby(by=['IdCliente'], as_index=False).agg({"IdTransacao": ['count'],'QtdePontos': ['sum', 'mean']})

sumary
# %%

sumary[('QtdePontos', 'mean')]
# %%

sumary.columns = ['Idcliente', 'qtdeTransacao', 'totalPontos', 'avgPontos']
sumary