import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import base64
import os

# Carregando os dados
df = pd.read_excel("RELATORIOS.xlsx", sheet_name='FROTA ANO A ANO')
df1 = pd.read_excel("RELATORIOS.xlsx", sheet_name='FROTA ATUAL')

# Definindo a primeira linha como cabeçalho e removendo essa linha do DataFrame
df1.columns = df1.iloc[0]
df1 = df1[1:]
df1.reset_index(drop=True, inplace=True)

# Criando uma cópia de df1 para manter os dados originais intactos
df1_total = df1.copy()
df1_municipio = df1[df1['Município'] != 'TOTAL DE VEÍCULOS DO ESTADO DO AMAPÁ']

# Carregando outros dados
df2 = pd.read_excel("RELATORIOS.xlsx", sheet_name='CONDUTORES POR ANO')
df3 = pd.read_excel("RELATORIOS.xlsx", sheet_name='INFRAÇÕES')

app = dash.Dash(__name__)

# Estilização customizada
def generate_table(dataframe):
    return html.Table(
        style={'width': '90%', 'margin': 'auto', 'borderCollapse': 'collapse', 'textAlign': 'center', 'fontFamily': 'Arial, sans-serif'},
        children=[
            html.Thead(
                html.Tr([html.Th(col, style={'border': '1px solid #ddd', 'padding': '10px', 'backgroundColor': '#4CAF50', 'color': 'white'}) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col], style={'border': '1px solid #ddd', 'padding': '8px'}) for col in dataframe.columns
                ]) for i in range(len(dataframe))
            ])
        ]
    )

# Convertendo a imagem para base64 com verificação de existência
image_path = "logo_detran.png"
encoded_image = ""
if os.path.exists(image_path):
    with open(image_path, 'rb') as f:
        encoded_image = base64.b64encode(f.read()).decode('ascii')
else:
    print("Imagem logo_detran.png não encontrada.")

# Layout da aplicação
app.layout = html.Div([
    # Menu de índice ao lado com fundo branco
    html.Div([
        html.H2('Índice', style={'textAlign': 'center', 'color': '#4CAF50', 'fontFamily': 'Arial, sans-serif'}),
        html.Ul([
            html.Li(html.A('Introdução', href='#introducao', style={'color': '#333', 'textDecoration': 'none'})),
            html.Li(html.A('Veículos por Município', href='#veiculos-municipio', style={'color': '#333', 'textDecoration': 'none'})),
            html.Li(html.A('Veículos por Ano', href='#veiculos-ano', style={'color': '#333', 'textDecoration': 'none'})),
            html.Li(html.A('Condutores por Ano', href='#condutores-ano', style={'color': '#333', 'textDecoration': 'none'})),
            html.Li(html.A('Infrações por Ano', href='#infracoes-ano', style={'color': '#333', 'textDecoration': 'none'})),
        ], style={'listStyleType': 'none', 'padding': 0, 'textAlign': 'left'})
    ], style={
        'width': '250px',
        'backgroundColor': '#f9f9f9',
        'padding': '20px',
        'position': 'fixed',
        'height': '100vh',
        'color': '#333',
        'overflow': 'auto',
        'borderRight': '1px solid #ddd'
    }),

    # Conteúdo principal
    html.Div([
        html.Div([
            # Imagem do logo
            html.Img(src=f'data:image/png;base64,{encoded_image}', style={'width': '15%', 'display': 'block', 'margin': '20px auto'}),
            html.H1('OBSERVATÓRIO DE TRÂNSITO', style={'textAlign': 'center', 'color': '#4CAF50', 'fontFamily': 'Arial, sans-serif'}),
        ]),
        
        # Introdução
        html.Div([
            html.H2('Introdução', id='introducao', style={'textAlign': 'center', 'color': '#555', 'fontFamily': 'Arial, sans-serif'}),
            html.P('Este relatório apresenta uma análise detalhada sobre a quantidade de veículos por município e dados sobre infrações de trânsito.', style={'textAlign': 'center', 'color': '#555'})
        ], style={'margin': '20px 0'}),
        
        # Veículos por município
        html.Div([
            html.H2('Quantidade de Veículos por Município em 2024', id='veiculos-municipio', style={'textAlign': 'center', 'color': '#555', 'fontFamily': 'Arial, sans-serif'}),
            dcc.Graph(
                id='FROTA ATUAL',
                figure=px.pie(df1_municipio, values='Quantidade de veículos', names='Município', title='Quantidade de veículos por município')
            ),
            generate_table(df1_total)
        ], style={'margin': '20px 0'}),
        
        # Veículos por ano
        html.Div([
            html.H2('Quantidade de Veículos por Ano', id='veiculos-ano', style={'textAlign': 'center', 'color': '#555', 'fontFamily': 'Arial, sans-serif'}),
            dcc.Graph(
                id='grafico-veiculos',
                figure=px.bar(df, x='ANO', y='Quantidade de veículos', title='Quantidade de veículos', color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
            ),
            generate_table(df)
        ], style={'margin': '20px 0'}),
        
        # Condutores por ano
        html.Div([
            html.H2('Quantidade de Condutores por Ano no Estado do Amapá', id='condutores-ano', style={'textAlign': 'center', 'color': '#555', 'fontFamily': 'Arial, sans-serif'}),
            dcc.Graph(
                id='grafico-condutores',
                figure=px.bar(df2, x='Ano', y='Quantidade de Condutores', title='Quantidade de condutores no estado do Amapá', color='Quantidade de Condutores', color_discrete_sequence=px.colors.qualitative.Set1)
            ),
            generate_table(df2)
        ], style={'margin': '20px 0'}),
        
        # Infrações cometidas por ano
        html.Div([
            html.H2('Quantidade de Infrações Cometidas por Ano no Estado do Amapá', id='infracoes-ano', style={'textAlign': 'center', 'color': '#555', 'fontFamily': 'Arial, sans-serif'}),
            dcc.Graph(
                id='grafico-infracoes',
                figure=px.bar(df3, x='ANO', y='TOTAL DE INFRAÇÕES', title='Quantidade de infrações por ano no estado do Amapá', color='TOTAL DE INFRAÇÕES', color_discrete_sequence=px.colors.qualitative.Set1)
            ),
            generate_table(df3)
        ], style={'margin': '20px 0'}),
        
    ], style={'marginLeft': '270px', 'padding': '20px'}),
    # Footer
    # Footer
html.Div([
    html.Hr(),
    html.P('Desenvolvido por DTIC - DEPARTAMENTO ESTADUAL DE TRÂNSITO DO AMAPÁ', style={'textAlign': 'center', 'color': '#555'}),
    html.P('Contato: cotec@detran.ap.gov.br', style={'textAlign': 'center', 'color': '#555'}),
    html.P('© 2024 Todos os direitos reservados.', style={'textAlign': 'center', 'color': '#555'})
], style={'marginTop': '50px', 'padding': '20px', 'backgroundColor': '#f9f9f9'})

])



# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)



 #html.Div([dash_table.DataTable(df, columns =["ANO", "Quantidade de veículos"])])
 