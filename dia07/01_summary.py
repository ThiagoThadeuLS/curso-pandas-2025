# %%

import pandas as pd

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
idades = pd.Series(idades)
idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()
# %%

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%

clientes['flTwitch'].sum()
clientes['flTwitch'].mean()
# %%

redes_sociais = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky','flInstagram']
clientes[redes_sociais].mean()
# %%

nun_columns = clientes.dtypes[~(clientes.dtypes == 'object')].index.to_list()
clientes[nun_columns].mean()
# %%

clientes[nun_columns].describe()