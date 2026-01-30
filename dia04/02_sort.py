# %%

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
max_ponto = clientes['qtdePontos'].max()
clientes[clientes['qtdePontos'] == max_ponto]
# %%

(clientes.sort_values(by='qtdePontos', ascending=False)
         .head()['idCliente'])