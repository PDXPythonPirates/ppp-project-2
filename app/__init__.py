from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import click
from sqlalchemy import exc
import time


# Construct core Flask application with embedded Dash app.
app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view='login'

from app import routes,models

# Initialize database - the db takes a bit of time to boot so retry
retries = 0
retry_limit = 10
while retries < retry_limit:
    try:
        click.echo(
            f"Flask initializing db using {app.config['SQLALCHEMY_DATABASE_URI']}"
        )
        db.create_all()
        click.echo(f"Successfully booted the db on try {retries + 1}")
        break
    except exc.SQLAlchemyError as error:
        retries += 1
        click.echo("Error: Issue connecting to the db. Look into this.")
        click.echo(f"{error}")
        time.sleep(5)


with app.app_context():
    # Import parts of our core Flask app
    from app import routes, errors, models  # noqa

    # Import Dash application
    from .plotly_dash.dashboard import init_dashboard

    app = init_dashboard(app)
