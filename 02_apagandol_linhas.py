import pandas as pd

pd.set_option('display.max_columns', 25)
pd.set_option('display.width', 2000)

table = pd.read_csv('storage/ClientesBanco.csv', encoding='latin1')

table = table.drop('CLIENTNUM', axis=1)
table = table.drop('Mudanças Transacoes_Q4_Q1', axis=1)
table = table.drop('Mudança Qtde Transações_Q4_Q1', axis=1)

table = table.dropna()
print(table.info())
