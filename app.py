from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config[SECRET_KEY] = 'chave-secreta'

@app.route("/")
def lista_de_tarefas():
    if 'lista' not in session:
        session['lista'] = []
    return render_template("tarefas.html", lista =session['lista'])

@app.route("/add", methods= ['POST'])
def add():
     lista = request.form.get('lista')
        session['lista'] = tarefa
        session.modified = True
    return redirect('/')
    
@app.route("/delete/<int:task_id>")
def remover(id_tarefa):

