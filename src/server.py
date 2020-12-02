from flask_graphql import GraphQLView
import config

from models import db
from app import app

db.init_app(app)
db.app = app

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
