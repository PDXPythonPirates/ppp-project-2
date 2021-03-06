from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config


# Construct core Flask application with embedded Dash app.
app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)

app.config.from_object(Config)


with app.app_context():
    # Import parts of our core Flask app
    from app import routes, errors  # noqa

    # Import Dash application
    from .plotly_dash.dashboard import init_dashboard

    app = init_dashboard(app)