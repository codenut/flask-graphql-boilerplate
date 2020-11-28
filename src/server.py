from flask import Flask
from flask_graphql import GraphQLView
import config

from models import db
from gql import schema

server = Flask(__name__)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

server.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema.schema, graphiql=True),
)

db.init_app(server)
db.app = server

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
