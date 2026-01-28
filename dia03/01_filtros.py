# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)


resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)

filtro = list(brinquedo['idade'] >= 18)
filtro

brinquedo[filtro]
# %%

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()

filtro = df['QtdePontos'] >= 50
df[filtro].head()
# %%

filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] >= 100)
df[filtro]

# %%

filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]
# %%

