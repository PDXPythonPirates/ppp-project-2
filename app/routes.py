from flask import render_template
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Fellow Pyrates"}
    posts = [
        {"author": {"username": "Sal"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Michael"}, "body": "Pyrates are so cool!"},
        {"author": {"username": "Scott"}, "body": "Ooh, Bootstrap!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)


@app.route("/register")
def register():
    return render_template("wip.html")
