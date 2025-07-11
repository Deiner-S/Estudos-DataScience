import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt





app = dash.Dash(__name__)


fig = px.line(df, x='Mês', y='Receita', title='Receita Mensal')

app.layout = html.Div(children=[
    html.H1('Relatório Financeiro'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)

