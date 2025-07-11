import plotly.express as px
import statistics as sts
import pandas as pd



def mediaGeral(figure,df_mensal):
    figure.add_hline(
        y=sts.median(df_mensal["Receita"]),
        line_dash="dash",
        line_color="#B305E6",
        annotation_text=f"Média: {sts.median(df_mensal["Receita"])}",
        annotation_position="top left"
    )
def mediaSeis(figure, df):
    data_limite = pd.to_datetime('2025-01')
    df['Periodos'] = pd.to_datetime(df['Periodos'])
    df_filtrado = df[df['Periodos'] >= data_limite]
    df_agrupado = df_filtrado.groupby(df_filtrado["Periodos"].dt.to_period("M"))['Receita'].sum().reset_index()
    figure.add_hline(
        y=sts.median(df_agrupado['Receita']),
        line_dash="dash",
        line_color="#6905E6",
        annotation_text=f"Últimos 6 mêses: {sts.median(df_agrupado['Receita'])}",
        annotation_position="bottom left"
    )
def FechamentoMes(df):
    df_mensal = df.groupby(df['DATA'].dt.to_period('M'))['TOTAL'].sum().reset_index()
    df_mensal.columns = ["Periodos", "Receita"]
    df_mensal['Periodos'] = df_mensal['Periodos'].dt.to_timestamp()
    df_mensal['Periodos'] = df_mensal['Periodos'].dt.strftime(r'%b/%Y')
    figure = px.bar(df_mensal,x="Periodos",y="Receita", title="Receita todo periodo")
    mediaGeral(figure,df_mensal)
    mediaSeis(figure, df_mensal)
    
    return figure

def MédiasEditora(df):

    sedufu = df[df["Editora"]== "EDUFU"]
    edufu = df.groupby(sedufu['DATA'].dt.to_period('M'))['TOTAL'].sum().reset_index()


    sunesp = df[df["Editora"]== "UNESP"]
    unesp = df.groupby(sunesp['DATA'].dt.to_period('M'))['TOTAL'].sum().reset_index()


    sufmg = df[df["Editora"]== "UFMG"]
    ufmg = df.groupby(sufmg['DATA'].dt.to_period('M'))['TOTAL'].sum().reset_index()

    medias  = pd.Series({"Media EDUFU":sts.median(edufu['TOTAL']),"UNESP":sts.median(unesp['TOTAL']),"UFMG":sts.median(ufmg['TOTAL'])}) 
    medias

    df_plot = medias.reset_index()
    df_plot.columns = ["Editoras", "Media"]
    figure = px.bar(df_plot,x="Editoras",y="Media", color="Editoras",title="Receita mensais de todo periodo")
    return figure

def graficoSetores(df):
    g = df.groupby(df['Editora'])['TOTAL'].sum().reset_index()
   
    fig = px.pie(
        g,
        names="Editora",
        values="TOTAL",
        title="Distribuição de Vendas por Editora",
        hole=0.3  # Estilo donut
    )

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',  # Mostra % e nome
        pull=[0.05]*len(g)  # Dá uma "explodidinha" em todas as fatias (opcional)
    )

    fig.update_layout(
        showlegend=True,
        legend_title_text='Editoras',
        #title_x=0.5
    )

    return fig