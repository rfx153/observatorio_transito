import dash
from dash import html
import base64

# Inicializando o app
app = dash.Dash(__name__)

# Convertendo a imagem para base64
image_path = "imagem.jpg"  # Altere para o nome da sua imagem
with open(image_path, 'rb') as f:
    encoded_image = base64.b64encode(f.read()).decode('ascii')

# Layout do app
app.layout = html.Div([
    html.H1("Exibindo uma Imagem no Dash"),
    html.Img(src=f'data:image/png;base64,{encoded_image}', style={'width': '50%'})
])

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)