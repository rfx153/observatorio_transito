
"""
import dash
from dash import dcc, html
import base64
##import pandas as pd
#import plotly.graph_objs as go

#df =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ANO A ANO')

# Carregando a imagem e convertendo para Base64
def encode_image(image_file):
    with open(image_file, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('ascii')
    return f'data:image/png;base64,{encoded}'
# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div(
    html.Img(src='imagem.jpg')
    #html.H1(children='Quantidade de Vseículos por Ano'),d

    #dcc.Graph(
    ##   figure=px.bar(df, x='ANO', y='Quantidade de veículos', title='Quantidade de veículos',color='Quantidade de veículos', color_discrete_sequence=px.colors.qualitative.Set1)
    #)
)

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)    
    
"""

#testando uma tabela 
from dash import Dash, html
import pandas as pd

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
df =pd.read_excel("RELATORIOS.xlsx",sheet_name='FROTA ANO A ANO')

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


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run(debug=True)