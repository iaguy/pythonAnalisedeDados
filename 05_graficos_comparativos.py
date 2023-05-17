import pandas as pd
import plotly.express as px
import os

if not os.path.exists("images"):
    os.mkdir("images")

table = pd.read_csv('storage/ClientesBanco.csv', encoding='latin1')

table = table.drop('CLIENTNUM', axis=1)
table = table.drop('Mudanças Transacoes_Q4_Q1', axis=1)
table = table.drop('Mudança Qtde Transações_Q4_Q1', axis=1)

for coluna in table:
    grafico = px.histogram(table, x=coluna, color="Categoria")
    grafico.write_image(f"images/{coluna}.pdf")

