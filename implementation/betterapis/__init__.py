import connexion
import logging
from connexion.resolver import RestyResolver
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.DEBUG)

api = connexion.FlaskApp(__name__, specification_dir='specs/')
api.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(api.app)
api.add_api('betterapis.yaml', resolver=RestyResolver('betterapis.controllers'))

