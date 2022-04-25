from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # database instance
migrate = Migrate(app, db)  # migration class

myBootstrapCSS = Bootstrap(app)

from app import routes, errors, models

# models: for database structure
