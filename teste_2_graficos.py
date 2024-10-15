import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


df =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ANO A ANO')#frita ano a ano é df
df1 =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ATUAL')#frota atual é df1
df1.columns = df1.iloc[0]
df1 = df1[df1['Município']!= 'TOTAL DE VEÍCULOS DO ESTADO DO AMAPÁ: ']
#apagar a linhas que tinha o nome das colunas
df1.drop(0, axis=0, inplace= True)
# Inicializando a aplicação Dash
app = dash.Dash(__name__)


# Layout da aplicação

app.layout = html.Div(
    children=[
    html.H1(['OBSERVATÓRIO DE TRÂNSITO DADOS']),
    html.Div([html.H1(children='Quantidade de Veículos por município em 2024'),
    dcc.Graph(
        id='FROTA ATUAL',
        figure=px.bar(df1, x='Município', y='Quantidade de veículos', title='Quantidade de veículos por município',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    )
]),
                 
    html.Div([
    html.H1(children='Quantidade de Veículos por Ano'),
    dcc.Graph(
        id='grafico-veiculos',
        figure=px.bar(df, x='ANO', y='Quantidade de veículos', title='Quantidade de veículos',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    )
])       
             
])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)

   

"""html.Div(children=[
    html.H1(children='Quantidade de Veículos por Ano'),

    dcc.Graph(
        id='grafico-veiculos',
        figure=px.bar(df, x='ANO', y='Quantidade de veículos', title='Quantidade de veículos',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    )
]),"""

"""
#fazendo mudanças no layout da aplicação

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Quantidade de Veículos por município em 2024'),

    dcc.Graph(
        id='FROTA ATUAL',
        figure=px.bar(df1, x='Município', y='Quantidade de veículos', title='Quantidade de veículos por município',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    )
])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)  
    
"""