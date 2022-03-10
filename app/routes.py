from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Fellow Pyrates"}
    posts = [
        {"author": {"username": "Sal"}, "body": "Beautiful day in Portland!"},

        
        {"author": {"username": "Michael"}, "body": "Pyrates are so cool!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
