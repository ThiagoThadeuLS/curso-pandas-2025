# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

# %%

import pandas as pd
import sqlalchemy
# %%

with open('03.sql') as open_file:
    query = open_file.read()
# %%

engine = sqlalchemy.create_engine('sqlite:///../../data/database.db')
clientes = pd.read_sql_query(query, con=engine)
# %%

clientes