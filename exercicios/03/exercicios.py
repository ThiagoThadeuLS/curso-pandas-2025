# %%
# 03.01 - Quantas linhas há no arquivo clientes.csv ?

import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
linhas = clientes.shape[0]

print(f'O arquivo de clientes.csv tem {linhas} linhas')
# %%
# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
print("O arquivo transacoes.csv tem uma coluna do tipo int (qtdePontos)")
# %%
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?

produtos = pd.read_csv('../../data/produtos.csv', sep=';')
produtos.dtypes
print("O arquivo produtos.csv tem cinco colunas do tipo int")
# %%
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.iloc[4]['idCliente']
# %%
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) 
# do arquivo clientes.csv ?

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.iloc[9]['qtdePontos']