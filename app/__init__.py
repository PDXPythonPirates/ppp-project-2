from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
myBootstrapCSS = Bootstrap(app)

from app import routes, errors  # noqa
