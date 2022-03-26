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
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    newLoginForm = LoginForm()
    if newLoginForm.validate_on_submit():
        errorMessage = (
            f"Login requested with info..."
            f"User:{newLoginForm.username.data}, "
            f"Password:{newLoginForm.password.data}, "
            f"Remember:{newLoginForm.remember_me.data}"
        )
        flash(errorMessage, "login_success")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=newLoginForm)


@app.route("/register")
def register():
    return render_template("wip.html")
