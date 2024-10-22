import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import base64
#arquivos utilizados
df =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ANO A ANO')#frita ano a ano é df
df1 =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ATUAL')#frota atual é df1
df1.columns = df1.iloc[0]
df1 = df1[df1['Município']!= 'TOTAL DE VEÍCULOS DO ESTADO DO AMAPÁ: ']
#apagar a linhas que tinha o nome das colunas
df1.drop(0, axis=0, inplace= True)
#condutores por ano
df2 = pd.read_excel("RELATORIOS.xlsx",sheet_name='CONDUTORES POR ANO')
#infrações por ano
df3 = pd.read_excel("RELATORIOS.xlsx",sheet_name='INFRAÇÕES')
# Inicializando a aplicação Dash
app = dash.Dash(__name__)

#função para gerar a tabela
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


#convertendo a imagem para base64
image_path = "logo_detran.png"  # Altere para o nome da sua imagem
with open(image_path, 'rb') as f:
    encoded_image = base64.b64encode(f.read()).decode('ascii')

# Layout da aplicação


app.layout = html.Div(
    children=[
    #imagem
    html.Img(src=f'data:image/png;base64,{encoded_image}', style={'width': '50%'}),
    html.H1(['OBSERVATÓRIO DE TRÂNSITO DETRAN AP']),
    html.Div([html.H1(children='Quantidade de Veículos por município em 2024'),
    dcc.Graph(
        id='FROTA ATUAL',
        #figure=px.pie(df1,values='Município', names='Quantidade de veículos', title='Quantidade de veículos por município',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
        figure = px.pie(df1,values='Quantidade de veículos', names='Município', title='Quantidade de veículos por município')  
    ),
    generate_table(df)
    
]),
   
                 
    html.Div([
    html.H1(children='Quantidade de Veículos por Ano'),
    dcc.Graph(
        id='grafico-veiculos',
        figure=px.bar(df, x='ANO', y='Quantidade de veículos', title='Quantidade de veículos',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    )
]),
    html.Div(children=[
    html.H1(children='Quantidade de condutores por ano no estado do amapá'),

    dcc.Graph(
        id='grafico-condutores',
        figure=px.bar(df2, x='Ano', y='Quantidade de Condutores', title='Quantidade de condutores no estado do amapá',color='Quantidade de Condutores', color_discrete_sequence=px.colors.qualitative.Set1)
    )
]),
    


    
       
             
])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)


 #html.Div([dash_table.DataTable(df, columns =["ANO", "Quantidade de veículos"])])
 