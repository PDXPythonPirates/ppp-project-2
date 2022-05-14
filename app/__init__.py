from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Construct core Flask application with embedded Dash app.
app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view='login'

from app import routes,models


with app.app_context():
    # Import parts of our core Flask app
    from app import routes, errors, models  # noqa

    # Import Dash application
    from .plotly_dash.dashboard import init_dashboard

    app = init_dashboard(app)