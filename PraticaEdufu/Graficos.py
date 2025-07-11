import plotly.express as px



def vendasMes(df):
    g = df.groupby(df["DATA"].dt.to_period("M")).size().sort_index()
    df_plot= g.reset_index()
    df_plot.columns = ["Periodos", "Vendas"]
    df_plot['Periodos'] = df_plot['Periodos'].dt.strftime('%b/%Y')
    fig = px.bar(df_plot,x="Periodos",y="Vendas", title="Vendas mensais de todo periodo")
    return fig

def vendasEditora(df):
    g1 = df.groupby(df["Editora"]).size()
    return g1.plot.bar(color= ['#4C6A71', '#5C715E', '#8C5E3C', '#B45F04', '#D6C4B0'])

def proporcao(df):
    g1 = df.groupby(df["Editora"]).size()
    # Total geral
    total = g1.sum()

    # Criar a legenda direto da Series
    legenda = [f"{categoria} - {valor/total:.1%}" for categoria, valor in g1.items()]

    # Plot
    fig, ax = plt.subplots()
    ax.pie(g1.values, labels=None, colors=['#4C6A71', '#B45F04', '#5C715E', '#8C5E3C', '#D6C4B0'], startangle=90)

    # Legenda lateral com nomes e porcentagens
    ax.legend(legenda, loc='center left', bbox_to_anchor=(1, 0.5), title="Categorias")

    # Título bonitinho
    ax.set_title("Distribuição por Categoria", fontsize=14)

    plt.tight_layout()
    plt.show()