# 06.01 - Qual a quantidade média de redes sociais dos usuários? 
# E a Variância? E o máximo?

# %%

import pandas as pd
# %%

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes['qtdeRedesSociais'] = (clientes['flEmail']+	
                                clientes['flTwitch']+	
                                clientes['flYouTube']+	
                                clientes['flBlueSky']+	
                                clientes['flInstagram']
                                )
clientes.describe()
# %%

clientes['qtdeRedesSociais'].mean()
# %%

clientes['qtdeRedesSociais'].var()
# %%

clientes['qtdeRedesSociais'].max()
# %%

clientes['qtdeRedesSociais'].agg(['mean', 'var', 'max'])