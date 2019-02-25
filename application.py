from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    a = 3
    b = 5
    if "x" not in session:
        session["x"] = a
    if session["x"] == 3:
        chal = "X"
    else:
        chal = "O"
    session["board"][row][col] = chal
    session["x"] = (a+b) - session["x"]

    return redirect(url_for("index"))
