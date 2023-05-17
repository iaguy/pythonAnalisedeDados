import pandas as pd

table = pd.read_csv('storage/ClientesBanco.csv', encoding='latin1')

print(table.info())
