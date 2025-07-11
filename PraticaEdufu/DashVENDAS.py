import dash
from dash import html, dcc
import pandas as pd
import Graficos as g

app = dash.Dash(__name__)

df = pd.read_csv("VENDAS.csv")

fig =  g.vendasMes(df)

app.layout = html.Div(children=[
    html.H1('Relatório Financeiro'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
