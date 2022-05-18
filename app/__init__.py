import click
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy import exc


# Construct core Flask application with embedded Dash app.
app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"


with app.app_context():
    # Import parts of our core Flask app
    from app import routes, errors, models, db  # noqa

    # Import Dash application
    from .plotly_dash.dashboard import init_dashboard

    # Initialize database
    click.echo(f"Flask initializing db using {app.config['SQLALCHEMY_DATABASE_URI']}")
    try:
        db.create_all()
    except exc.SQLAlchemyError as error:
        click.echo("Error: Issue connecting to the db. Look into this.")
        click.echo(f"{error}")

    # Initialize dahsboard
    app = init_dashboard(app)
