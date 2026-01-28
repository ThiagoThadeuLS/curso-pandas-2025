# %%

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%

filtro = clientes['qtdePontos'] == 0
cliente_0 = clientes[filtro].copy()

cliente_0['flag_1'] = 1
cliente_0
# %%

clientes 