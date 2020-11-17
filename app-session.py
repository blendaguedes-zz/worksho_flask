from flask import Flask, render_template, request, session, make_response
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route('/note')
def note():
    if session.get("notes") is None:
        session["notes"] = []
    return render_template('note/todo.html', title='Things to Do', notes=session["notes"])


@app.route('/note/add', methods=["POST"])
def add_note():
    if session.get("notes") is None:
        session["notes"] = []
    note = request.form.get("note")
    session["notes"].append(note)
    return render_template("note/todo.html", title='Things to Do', notes=session["notes"])


@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    return res
#
# @app.route('/note/add', methods=["POST"])
# def add_note():
#     if session.get("notes") is None:
#         session["notes"] = []
#     note = request.form.get("note")
#     session["notes"].append(note)
#     return render_template("note/todo.html", title='Things to Do', notes=session["notes"])
