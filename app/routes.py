from flask import render_template, flash, redirect, url_for
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
        {"author": {"username": "Allyson"}, "body": "Hello, World!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, "
            f"remember_me={form.remember_me.data}"
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Log In", form=form)


@app.route("/register")
def register():
    return render_template("wip.html")
