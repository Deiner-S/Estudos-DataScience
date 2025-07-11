import plotly.express as px
import statistics as sts
import pandas as pd
def mediaGeral(figure,df_agrupado):
    figure.add_hline(
        y=sts.median(df_agrupado),
        line_dash="dash",
        line_color="#B305E6",
        annotation_text=f"Média: {sts.median(df_agrupado)}",
        annotation_position="top left"
    )
def mediaSeis(figure, df):
    data_limite = pd.to_datetime('2025-01')
    df_filtrado = df[df['DATA'] >= data_limite]
    df_agrupado = df_filtrado.groupby(df_filtrado["DATA"].dt.to_period("M")).size().sort_index()
    figure.add_hline(
        y=sts.median(df_agrupado),
        line_dash="dash",
        line_color="#6905E6",
        annotation_text=f"Últimos 6 mêses: {sts.median(df_agrupado)}",
        annotation_position="top left"
    )

def vendasMes(df):
    df_agrupado = df.groupby(df["DATA"].dt.to_period("M")).size().sort_index()
    df_plot= df_agrupado.reset_index()
    df_plot.columns = ["Periodos", "Vendas"]
    df_plot['Periodos'] = df_plot['Periodos'].dt.to_timestamp()
    df_plot['Periodos'] = df_plot['Periodos'].dt.strftime('%b/%Y')
    figure = px.bar(df_plot,x="Periodos",y="Vendas", title="Vendas mensais de todo periodo")
    mediaGeral(figure,df_agrupado)
    mediaSeis(figure, df)
    
    return figure

def MédiasEditora(df):

    sedufu = df.loc[df["Editora"]== "EDUFU", "DATA"]
    edufu = df.groupby(sedufu.dt.to_period("M")).size().sort_index()


    sunesp = df.loc[df["Editora"]== "UNESP", "DATA"]
    unesp = df.groupby(sunesp.dt.to_period("M")).size().sort_index()


    sufmg = df.loc[df["Editora"]== "UFMG", "DATA"]
    ufmg = df.groupby(sufmg.dt.to_period("M")).size().sort_index()

    medias  = pd.Series({"Media EDUFU":sts.median(edufu),"UNESP":sts.median(unesp),"UFMG":sts.median(ufmg)}) 
    medias

    df_plot = medias.reset_index()
    df_plot.columns = ["Editoras", "Media"]
    figure = px.bar(df_plot,x="Editoras",y="Media", color="Editoras",title="Vendas mensais de todo periodo")
    return figure

def graficoSetores(df):
    g = df.groupby("Editora").size().reset_index(name="Vendas")

    fig = px.pie(
        g,
        names="Editora",
        values="Vendas",
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