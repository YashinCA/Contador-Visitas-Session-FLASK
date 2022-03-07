from flask import Flask, render_template, request, redirect, session
import base64


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    session['contador'] = 0
    session['cantidadUsuarioTotal'] = 0

    print(session['contador'])
    return redirect("/contar")


@app.route("/contar")
def contar():
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    session['cantidadUsuarioTotal'] = 0
    # print("#################################### \n ")
    # print(base64.urlsafe_b64decode(
    #     "eyJjYW50aWRhZFVzdWFyaW9Ub3RhbCI6MCwiY29udGFkb3IiOjF9==="))
    # print("#################################### \n")
    return render_template('contador.html', contador=session['contador'], cantidadUsuarioTotal=session['cantidadUsuarioTotal'])


@app.route("/contar", methods=['POST'])
def agregar():
    print(request.form)
    print(request.form['agregar'])
    cantidad = int(request.form['agregar'])
    session['contador'] += cantidad
    session['cantidadUsuarioTotal'] = session['cantidadUsuarioTotal']
    # print("#################################### \n ")
    # print(base64.urlsafe_b64decode(
    #     "eyJjYW50aWRhZFVzdWFyaW9Ub3RhbCI6MCwiY29udGFkb3IiOjF9==="))
    # print("#################################### \n")
    return render_template('contador.html', contador=session['contador'], cantidadUsuarioTotal=session['cantidadUsuarioTotal'])


@app.route("/agregarmanual", methods=['POST'])
def agregarUsuario():
    print(request.form)
    print(request.form['cantidadform'])
    cantidadUsuario = int(request.form['cantidadform'])
    session['cantidadUsuarioTotal'] += cantidadUsuario
    session['contador'] += cantidadUsuario
    # print("#################################### \n ")
    # print(base64.urlsafe_b64decode(
    #     "eyJjYW50aWRhZFVzdWFyaW9Ub3RhbCI6MCwiY29udGFkb3IiOjF9==="))
    # print("#################################### \n")
    return render_template('contador.html', contador=session['contador'], cantidadUsuarioTotal=session['cantidadUsuarioTotal'])
    # redirect


@app.route("/destroy")
def destruir():
    if 'contador' in session:
        session.pop('contador')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
