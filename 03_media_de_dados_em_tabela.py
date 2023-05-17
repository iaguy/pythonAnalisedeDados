import pandas as pd

pd.set_option('display.max_columns', 25)  # Seleciona o número máximo de colunas a serem exibidas
pd.set_option('display.width', 2000)  # Seleciona a largura do display

table = pd.read_csv('storage/ClientesBanco.csv', encoding='latin1')
dados_media = table.describe().round(1)
print(dados_media)
