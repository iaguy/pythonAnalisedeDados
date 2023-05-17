import pandas as pd

pd.set_option('display.max_columns', 25)  # Seleciona o número máximo de colunas a serem exibidas
pd.set_option('display.width', 2000)  # Seleciona a largura do display

table = pd.read_csv('storage/ClientesBanco.csv', encoding='latin1')

qtd_categoria = table["Categoria"].value_counts()
qtd_categoria_porcentagem = table["Categoria"].value_counts(normalize=True)

print(qtd_categoria), print(qtd_categoria_porcentagem)
