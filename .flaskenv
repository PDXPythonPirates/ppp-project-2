# flask run uses this file to set configs (prod config overrites these)
FLASK_APP=app_run.py
FLASK_ENV=development
FLASK_DEBUG=true
# database format info for sqlalchemy *://username:password@host:port/database_name
# sqlLite-sqlalchemy config
DATABASE_URL = mysql+pymysql://pyrate:iamyourcaptain@localhost:3306/pyrates