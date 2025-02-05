import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import base64

# Carregando os dados
df = pd.read_excel("RELATORIOS.xlsx", sheet_name='FROTA ANO A ANO')
df1 = pd.read_excel("RELATORIOS.xlsx", sheet_name='FROTA ATUAL')
df1.columns = df1.iloc[0]
df1 = df1[df1['Município'] != 'TOTAL DE VEÍCULOS DO ESTADO DO AMAPÁ: ']
df1.drop(0, axis=0, inplace=True)

df2 = pd.read_excel("RELATORIOS.xlsx", sheet_name='CONDUTORES POR ANO')
df3 = pd.read_excel("RELATORIOS.xlsx", sheet_name='INFRAÇÕES')
# Inicializando a aplicação Dash
app = dash.Dash(__name__)

#função para gerar a tabela
def generate_table(dataframe):
    return html.Table(
        # Estilo da tabela
        style={'width': '80%', 'margin': 'auto', 'borderCollapse': 'collapse', 'textAlign': 'center'},
        children=[
            html.Thead(
                html.Tr([html.Th(col, style={'border': '1px solid black', 'padding': '8px', 'backgroundColor': '#f2f2f2'}) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col], style={'border': '1px solid black', 'padding': '8px'}) for col in dataframe.columns
                ]) for i in range(len(dataframe))
            ])
        ]
    )


#convertendo a imagem para base64
image_path = "logo_detran.png"  # Altere para o nome da sua imagem
with open(image_path, 'rb') as f:
    encoded_image = base64.b64encode(f.read()).decode('ascii')

# Layout da aplicação


app.layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f9f9f9', 'padding': '20px'},
    children=[
        # Imagem e título
        html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_image}', style={'width': '20%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.H1('OBSERVATÓRIO DE TRÂNSITO', style={'textAlign': 'center', 'color': '#333'}),
        ]),
        
        # Índice
        html.Div([
            html.H2('Índice', style={'textAlign': 'center', 'color': '#555'}),
            html.Ul([
            html.Li(html.A('Introdução', href='#introducao')),
            html.Li(html.A('Quantidade de Veículos por Município em 2024', href='#veiculos-municipio')),
            html.Li(html.A('Quantidade de Veículos por Ano', href='#veiculos-ano')),
            html.Li(html.A('Quantidade de Condutores por Ano no Estado do Amapá', href='#condutores-ano')),
            html.Li(html.A('Quantidade de Infrações Cometidas por Ano no Estado do Amapá', href='#infracoes-ano')),
            ], style={'listStyleType': 'none', 'padding': 0, 'textAlign': 'center'})
        ], style={'margin': '20px 0'}),
        
        
        
        # Introdução
        html.Div([
            html.H2('Introdução', id='introducao', style={'textAlign': 'center', 'color': '#555'}),
            html.P('Este relatório apresenta uma análise detalhada sobre a quantidade de veículos por município, além de fornecer dados sobre a quantidade de veículos registrados e as respectivas infrações de trânsito (multas) ocorridas em cada localidade. As informações contidas neste documento visam fornecer uma visão abrangente do panorama atual de veículos e suas respectivas infrações em diferentes regiões, permitindo identificar padrões de comportamento e áreas que necessitam de maior atenção para o aprimoramento das políticas de trânsito e segurança pública. A partir dos dados apresentados, é possível entender a distribuição dos veículos em todo o território, bem como a correlação entre o número de veículos e o volume de multas aplicadas, contribuindo para a análise e planejamento de estratégias mais eficazes no controle e fiscalização do trânsito.', style={'textAlign': 'center', 'color': '#555'})
        ], style={'margin': '20px 0'}),
        # Veículos por município
        html.Div([
            html.H2('Quantidade de Veículos por Município em 2024', id='veiculos-municipio', style={'textAlign': 'center', 'color': '#555'}),
            dcc.Graph(
                id='FROTA ATUAL',
                figure=px.pie(df1, values='Quantidade de veículos', names='Município', title='Quantidade de veículos por município')
            ),
            generate_table(df1)
        ], style={'margin': '20px 0'}),
        
        # Veículos por ano
        html.Div([
            html.H2('Quantidade de Veículos por Ano', id='veiculos-ano', style={'textAlign': 'center', 'color': '#555'}),
            dcc.Graph(
                id='grafico-veiculos',
                figure=px.bar(df, x='ANO', y='Quantidade de veículos', title='Quantidade de veículos', color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
            ),
            generate_table(df)
        ], style={'margin': '20px 0'}),
        
        # Condutores por ano
        html.Div([
            html.H2('Quantidade de Condutores por Ano no Estado do Amapá', id='condutores-ano', style={'textAlign': 'center', 'color': '#555'}),
            dcc.Graph(
                id='grafico-condutores',
                figure=px.bar(df2, x='Ano', y='Quantidade de Condutores', title='Quantidade de condutores no estado do Amapá', color='Quantidade de Condutores', color_discrete_sequence=px.colors.qualitative.Set1)
            ),
            generate_table(df2)
        ], style={'margin': '20px 0'}),
        
        # Infrações cometidas por ano
        html.Div([
            html.H2('Quantidade de Infrações Cometidas por Ano no Estado do Amapá', id='infracoes-ano', style={'textAlign': 'center', 'color': '#555'}),
            dcc.Graph(
                id='grafico-infracoes',
                figure=px.bar(df3, x='ANO', y='TOTAL DE INFRAÇÕES', title='Quantidade de infrações por ano no estado do Amapá', color='TOTAL DE INFRAÇÕES', color_discrete_sequence=px.colors.qualitative.Set1)
            ),
            generate_table(df3)
        ], style={'margin': '20px 0'}),
        
    ]
)

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)


 #html.Div([dash_table.DataTable(df, columns =["ANO", "Quantidade de veículos"])])
 