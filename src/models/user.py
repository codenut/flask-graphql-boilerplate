"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "users"

    username = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(128), primary_key=True)

    def __init__(self, username, email):
        """ Create a new User """
        self.username = username
        self.email = email
