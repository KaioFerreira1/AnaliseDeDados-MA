from flask import *
import dao
import dataanalise as da
import plotly.express as px

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def cadastrar_usuario():
    nome = str(request.form.get('nome'))
    senha = str(request.form.get('senha'))

    if dao.verificarlogin(nome, senha):
        return render_template('menu.html')
    else:
        return render_template('index2.html')

@app.route('/grafvioleciapib', methods=['POST', 'GET'])
def gerarGrafViolenciaPib():
    if request.method == 'POST':
        filtro = int(request.form.get('valor'))
    else:
        filtro = 10

    dados = da.lerdados()
    dados.drop(dados.sort_values(by=['cvli'], ascending=False).head(3).index, inplace=True)
    dados.drop(dados.sort_values(by=['rendapercapita'], ascending=False).head(filtro).index, inplace=True)
    dados.drop(dados.sort_values(by=['rendapercapita'], ascending=True).head(2).index, inplace=True)

    fig = px.scatter(dados, x='rendapercapita', y='cvli', hover_data=['municipio'])
    return render_template('grafviolenciapib.html', plot=fig.to_html())

@app.route('/grafcorrelacao')
def gerarGrafCorrelacao():
    dados = da.lerdados()
    fig2 = da.exibirmapacorrelacoes(dados)

    return render_template('grafcorrelacao.html', mapa=fig2.to_html())

@app.route('/grafidh', methods=['POST', 'GET'])
def gerarGrafIDH():
    if request.method == 'POST':
        filtro = int(request.form.get('valor'))
    else:
        filtro = 10  # Corrigindo aqui, você precisa definir um valor padrão

    dados = da.lerdados()
    dados = dados.sort_values(by=['rendapercapita'], ascending=True)
    dados = dados.iloc[filtro:]  # Aplicando o filtro aos dados
    fig3 = da.exibir_mapa_idh(dados)
    return render_template('grafidh.html', mapa=fig3.to_html())

@app.route('/grafcvlivsidh', methods=['POST', 'GET'])
def gerarGrafCVLIvsIDH():
    if request.method == 'POST':
        num_estados = int(request.form.get('num_estados'))
    else:
        num_estados = 10
    dados = da.lerdados()
    fig4 = da.exibir_graf_cvli_x_idh(dados, num_estados)
    return render_template('grafcvlivsidh.html', mapa=fig4.to_html())


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/')
def motormanda():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
