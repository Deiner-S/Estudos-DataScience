import dash
from dash import html, dcc, Input, Output
import pandas as pd
import Graficos as gr
import Fechamento as fto


app = dash.Dash(__name__)

df = pd.read_csv(r"VENDAS2.csv")
df["DATA"] = pd.to_datetime(df["DATA"]) 

app.layout = html.Div([

    html.Header([html.H1('Painel de Desempenho financeiro')]),    
    
    html.Div([
        html.Button("Vendas", id= "btn-1",n_clicks=0, className="button hover"),
        html.Button("Receita", id= "btn-2",n_clicks=0, className="button hover")
    ],className="div-button"),

    html.Div(id="dashboard-content")

],className="home")






@app.callback(
    Output("dashboard-content", "children"),
    [Input("btn-1","n_clicks"), Input("btn-2","n_clicks")]
)
def display_dashboard(n1,n2):
    context = dash.callback_context
    if not context.triggered:
        return html.Div([
    html.H2("Resumo de vendas"),
    html.Div([
        dcc.Graph(figure=gr.vendasMes(df)),
        dcc.Graph(figure=gr.MédiasEditora(df)),
        dcc.Graph(figure=gr.graficoSetores(df)),
        dcc.Graph(figure=gr.online()),
        
        ], className= "dashboard"),
])
    button_id = context.triggered[0]["prop_id"].split(".")[0]
    if button_id == "btn-1":
        return html.Div([
        html.H2("Resumo de vendas"),
        html.Div([
        dcc.Graph(figure=gr.vendasMes(df)),
        dcc.Graph(figure=gr.MédiasEditora(df)),
        dcc.Graph(figure=gr.graficoSetores(df)),
        dcc.Graph(figure=gr.online()),        
        ], className= "dashboard"),
])

    elif button_id == "btn-2":
        return html.Div([
        html.H2("Resumo de receita"),
        html.Div([
        dcc.Graph(figure=fto.FechamentoMes(df)),
        dcc.Graph(figure=fto.MédiasEditora(df)),
        dcc.Graph(figure=fto.graficoSetores(df)),
        dcc.Graph(figure=fto.online())
        
        ], className= "dashboard"),
])

if __name__ == '__main__':
    app.run(debug=True)
