### Desafio de analise de uma base dados de um administradora de cartões que tem seus clientes cancelando o produto. Analise o porque da desistencia dos clientes

'''import pandas as pd
import plotly.express as px'''

'''pd.set_option('display.max_columns', 25)  # Seleciona o número máximo de colunas a serem exibidas
pd.set_option('display.width', 2000)  # Seleciona a largura do display

table = pd.read_csv('storage/ClientesBanco.csv', encoding='latin1')'''

# Excluindo colunas denescessarias para analise

'''table = table.drop('CLIENTNUM', axis=1)  
table = table.drop('Mudanças Transacoes_Q4_Q1', axis=1) 
table = table.drop('Mudança Qtde Transações_Q4_Q1', axis=1)'''

''' print(table.info())   'Faz a verificação dos campos que nao estão em brancos'
    table = table.dropna()   'Excluir todas as linhas com valores vazios' '''

_Método describe() utiliza para ver como estão alocados dos dados da tabela (quantos itens tem em cada tabela,
 a media, a minima, a maxima, SOMENTE PARA COLUNAS COM NUMEROS_
 
_'print(table.describe().round(1))' para arrendondar valores utiliza o metodo round seguido do tantos de casa deciamais 
para arredonddar_

'''dados_media = table.describe().round(1)

print(dados_media)'''

# Analise de clientes x cancelamentos

'''qtd_categoria = table["Categoria"].value_counts() 
qtd_categoria_porcentagem = table["Categoria"].value_counts(normalize=True)

_value.counts() metodo para contagem dos valores dentro do objeto_
print(qtd_categoria), print(qtd_categoria_porcentagem)
_Podemos ter varias formas de verificar o motivo do cancelamento
    - Pode-se comparar cliente x cancelados em cada coluna da base de dados para validar possivel motivo de desistencia
    e mostar em graficos com a biblioteca plotly_
> 
'''grafico = px.histogram(table, x="Idade", color="Categoria")
grafico.show()'''

_Podemos fazer interações com FOR dentro da tababela para analise de varios valores
OBS.: for em tabelas ele por padrao faz pelas colunas, para linha seria for linha in table.index_
 
'''   for coluna in table:
        grafico = px.histogram(table, x=coluna, color="Categoria")
        grafico.show()'''
