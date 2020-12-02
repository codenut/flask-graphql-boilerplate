from flask import Flask
from flask_bcrypt import Bcrypt
from flask_graphql import GraphQLView
import config

from gql import schema

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.debug = config.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql",
                                  schema=schema.schema,
                                  graphiql=True),
)
