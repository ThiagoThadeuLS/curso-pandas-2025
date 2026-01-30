# %%

import pandas as pd
import numpy as np

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
# %%

df['pontos_100'] = df['qtdePontos'] * 100
# %%

df['email-Twitch'] = df['flEmail'] + df['flTwitch']
df.head()
# %%

df['flEmail'] * df['flTwitch']
# %%

df['qtdeSocial'] = df['flEmail'] + df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']	
df
# %%

df['todas'] = df['flEmail'] * df['flTwitch'] * df['flYouTube'] * df['flBlueSky'] * df['flInstagram']	
df
# %%

df['qtdePontos'].describe()


# %%

df['logPontos'] = np.log(df['qtdePontos'] + 1)
df['logPontos'].describe()
# %%

