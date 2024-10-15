# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:16:24 2024

@author: rafael.cardoso
"""

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


df =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ATUAL')
df.columns = df.iloc[0]
df = df[df['Município']!= 'TOTAL DE VEÍCULOS DO ESTADO DO AMAPÁ: ']
#apagar a linhas que tinha o nome das colunas
df.drop(0, axis=0, inplace= True)
# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Quantidade de Veículos por município em 2024'),

    dcc.Graph(
        id='FROTA ATUAL',
        figure=px.bar(df, x='Município', y='Quantidade de veículos', title='Quantidade de veículos por município',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    )
])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
"""
#utilizando somente o plotly

fig = px.bar(x=df["ANO"], y=df["Quantidade de veículos"], labels={'x': 'Ano', 'y': 'Quantidade de Veículos'})

# Adicionar título ao gráfico
fig.update_layout(title='FROTA NO ESTADO DO AMAPÁ NOS ÚLTIMOS ANOS')
# Tabela 

fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['ANO'], df["Quantidade de veículos"]],
               fill_color='lavender',
               align='left'))
])
"""
# Exibir o gráfico
#fig.show()
#fig_table.show()
#fig.write_image('frota_ano_ano.png')
