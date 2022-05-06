import click
from app import app, db  # noqa
from app.models import User, Coin


# use `flask shell` to pre-import these in the shell context
# Usage: `db`, `User`, `Coin`
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Coin": Coin}


# docker usage: docker-compose exec flask-app flask create_db
@app.cli.command("create_db")
def create_db():
    click.echo("Initializing the db")
    db.drop_all()
    db.create_all()
    db.session.commit()


@app.cli.command("seed_db")
def seed_db():
    click.echo("Seeding the db")
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()
