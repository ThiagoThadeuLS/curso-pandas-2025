# 06.05 - Qual a média de transações / dia?

# %%
import pandas as pd

# %%

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%

transacoes['DtCriacao'] = pd.to_datetime(transacoes['DtCriacao'])
transacoes['data'] = transacoes['DtCriacao'].dt.date
transacoes.head()
# %%

df = pd.DataFrame(transacoes.groupby(by='data')['IdTransacao'].count())
# %%

df.describe()
# %%