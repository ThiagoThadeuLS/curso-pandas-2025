# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df
# %%

df.shape
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%

renamed_columns = {
    'QtdePontos': 'qtPontos',
    'DescSistemaOrigem': 'sistemaOrigem'
}

# df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True)

# %%

colunas = ['IdCliente', 'qtPontos']
df[colunas]
# %%

# SELECT * FROM df
df
# %%
# SELECT idCliente FROM df

df[["idCliente"]]
# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5
df[["idCliente", "qtPontos"]].tail(5)
# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

df[["idCliente", "idTransacao", "qtPontos"]].head(5)
# %%

colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df