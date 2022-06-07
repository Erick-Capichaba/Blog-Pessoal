from distutils.log import debug
import string
from flask import Flask, Request, render_template

#route = Caminho que vem depois do dominio da pagina.
#função 0 Oque estará dentro do site.

 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def Homepage():
    return render_template('HomepageViews.html')

@app.route('/contatos')
def contato():
    return render_template('ContatosViews.html')

@app.route("/about")
def about():
    return render_template('aboutviews.html')

@app.route('/<string:nome>')
def erro(nome):
    return f'<font size="25" color="red" >Desculpe mas a página <b>{nome}</b> não existe!</font>'

@app.route("/post")
def post():

    
     return render_template ('PostViews.html')
    
@app.route("/post2", methods=['GET'])
def direcionar():
    return 


if __name__ == '__main__':
    app.run(debug=True)
