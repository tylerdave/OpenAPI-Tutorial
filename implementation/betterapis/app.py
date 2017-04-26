import connexion
from connexion.resolver import RestyResolver
from flask_sqlalchemy import SQLAlchemy

# Uncomment to see import-time debug logging:
#import logging
#logging.basicConfig(level=logging.DEBUG)

api = connexion.FlaskApp(__name__, specification_dir='specs/')
api.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/betterapis.db'
api.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api.app)
api.add_api('betterapis.yaml', resolver=RestyResolver('betterapis.controllers'))

