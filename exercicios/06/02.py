# 06.02 - Quais são os usuários que mais fizeram transações? 
# Considere os 10 primeiros.

# %%

import pandas as pd
import sqlalchemy
# %%

with open('02.sql') as open_file:
    query = open_file.read()

print(query)
# %%

engine = sqlalchemy.create_engine('sqlite:///../../data/database.db')
clientes = pd.read_sql_query(query, con=engine)
clientes
# %%
