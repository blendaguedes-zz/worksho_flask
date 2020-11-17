from flask import Flask, render_template, request

app = Flask(__name__)

notes = []


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route("/template")
def hello_template():
    palavras = "Todos aprovados! Parabéns!"
    return render_template('hello.html', mensagem="Todos aprovados! Parabéns!")


@app.route("/test/<string:argumento>")
def argumento(argumento):
    return render_template('hello.html', nome=argumento)


@app.route("/note/fav", methods=["GET"])
def favorite_champ():
    return render_template('note/fav.html')

@app.route("/d", methods=["POST"])
def dd():
    a = request.args.get('a')
    return a

@app.route("/fav/<string:name>")
def fav(name):
    is_lux = True if name.upper() == "LUX" else False
    name = name.capitalize()
    return render_template('fav.html', champion=name, is_lux=is_lux)


@app.route("/note/fav", methods=["POST"])
def submit_champ():
    name = request.form.get("champ")
    is_lux = True if name.upper() == "LUX" else False
    name = name.capitalize()
    return render_template('note/fav.html', champion=name, is_lux=is_lux)


# @app.route("/note/fav", methods=["POST", "GET"])
# def submit_champ():
#     if request.method == "GET":
#         return render_template('note/fav.html')
#     else:
#         name = request.form.get("name")
#         is_lux = True if name.upper() == "LUX" else False
#         name = name.capitalize()
#         return render_template('note/fav.html', champion=name, is_lux=is_lux)


@app.route('/note')
def note():
    return render_template('note/todo.html', title='Coisas para fazer', notes=notes)


@app.route('/note/add', methods=["POST"])
def add_note():
    note = request.form.get("note")
    notes.append(note)
    return render_template("note/todo.html", title='Coisas para fazer', notes=notes)
