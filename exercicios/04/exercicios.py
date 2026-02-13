# %%
# 04.01 - Quantos clientes tem vínculo com a Twitch?

import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()

filtro = list(clientes['flTwitch'] == 1)
qtde_twitch = clientes[filtro]['flTwitch'].shape[0]

print(f'Temos {qtde_twitch} usuários com twitch')
# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

qtde_1000 = clientes[list(clientes['qtdePontos'] > 1000)]['qtdePontos'].shape[0]
print(f"Temos {qtde_1000} clientes com mais de 1000 pontos")
# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

import datetime 

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes['DtCriacao'] = pd.to_datetime(transacoes['DtCriacao']).dt.date
qtde_dia = transacoes[list(transacoes['DtCriacao'] == datetime.date(2025, 2, 1))]['IdTransacao'].shape[0]
print(f"No dia 2025-02-01 tivemos {qtde_dia} transacoes")