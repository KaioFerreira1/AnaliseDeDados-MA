import pandas as pd
import plotly.express as px

def analisar():
    dados = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_taxa_de_homic%C3%ADdios')
    mais250 = dados[0]
    menores = dados[1]
    print(dados[0])

def lerdados():
    dados = pd.read_csv('dadosindicadoresPB3.csv')
    #excluir colunas
    dados.drop(columns=['code'], inplace=True)
    return dados

def exibirmapacorrelacoes(data):
    data.drop(columns=['municipio'], inplace=True)
    fig = px.imshow(data.corr())
    return fig


def exibir_mapa_idh(data):
    fig = px.scatter(data, x='idh', y='rendapercapita', color='municipio')
    return fig

def exibir_graf_cvli_x_idh(data, num_estados=10):
    data = data.sort_values(by='idh', ascending=False)
    data = data.head(num_estados)
    fig = px.bar(data, x='idh', y='cvli', color='municipio')
    return fig
