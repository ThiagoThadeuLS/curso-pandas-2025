# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
# %%

idCliente = '0033b737-8235-4c0f-9801-dc4ca185af00'

def get_last_id(x):
    return x.split('-')[-1]
# %%

get_last_id('0028dda2-334f-40bb-9582-475fb6719471')
# %%

id_novo = []

for i in df['idCliente']:
    novo = get_last_id(i)
    id_novo.append(novo)

df['novo_id'] = id_novo
df.head()
# %%

df['idCliente'].apply(get_last_id)