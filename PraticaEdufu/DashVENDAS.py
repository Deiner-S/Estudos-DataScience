import dash
from dash import html, dcc
import pandas as pd
import Graficos as gr
import Fechamento as fto


app = dash.Dash(__name__)

df = pd.read_csv(r"VENDAS2.csv")
df["DATA"] = pd.to_datetime(df["DATA"]) 







app.layout = html.Div([

    
    html.H1('Painel de Desempenho financeiro', style={
            'color': '#FFFFFF',
            'textAlign': 'center',
            'fontSize': '48px',
            'fontWeight': 'bold',
            'fontFamily': 'Segoe UI, sans-serif',
            'padding': '30px',
            'textShadow': '1px 1px 4px #000',
            'margin': '0',
    }),

    html.Div([html.H2("Resumo de vendas",style={
    'color': '#FFFFFF',
    'textAlign': 'center',
    'fontSize': '32px',
    'fontWeight': '600',
    'fontFamily': 'Segoe UI, sans-serif',
    'padding': '10px 0',
    'marginTop': '50px',  # margem superior maior pra separar bem do conteúdo acima
    'marginBottom': '5px',
    'textShadow': '1px 1px 3px #000',
    
    })]),

    html.Div([
        dcc.Graph(figure=gr.vendasMes(df)),
        dcc.Graph(figure=gr.MédiasEditora(df)),
        dcc.Graph(figure=gr.graficoSetores(df)),
        
    ], style={
    'display': 'flex',
    'flexWrap': 'wrap',  # 💥 ESSA LINHA faz ele quebrar de linha
    'gap': '20px',
    'justifyContent': 'center',  # opcional: centraliza os gráficos
    'padding': '20px',
    
    }),

    html.Div([html.H2("Receita",style={
    'color': '#FFFFFF',
    'textAlign': 'center',
    'fontSize': '32px',
    'fontWeight': '600',
    'fontFamily': 'Segoe UI, sans-serif',
    'padding': '10px 0',
    'marginTop': '50px',  # margem superior maior pra separar bem do conteúdo acima
    'marginBottom': '5px',
    'textShadow': '1px 1px 3px #000',
  
    })]),

    html.Div([
        dcc.Graph(figure=fto.FechamentoMes(df)),
        dcc.Graph(figure=fto.MédiasEditora(df)),
        dcc.Graph(figure=fto.graficoSetores(df)),
        
    ], style={
    'display': 'flex',
    'flexWrap': 'wrap',  # 💥 ESSA LINHA faz ele quebrar de linha
    'gap': '20px',
    'justifyContent': 'center',  # opcional: centraliza os gráficos
    'padding': '20px',
 
    }),
    
    

],style={
    'backgroundImage': 'url("assets/padrao.jpg")',
    'backgroundRepeat': 'repeat',             # permite repetir em X e Y
    'backgroundSize': 'auto',                 # usa o tamanho real da imagem
    'backgroundPosition': 'top left',         # começa no canto superior esquerdo
    'minHeight': '100vh',                     # cobre toda a altura da tela
    'width': '100%',
    'padding': '20px',
    'boxSizing': 'border-box',  # Remove scrollbar lateral
    })

if __name__ == '__main__':
    app.run(debug=True)
