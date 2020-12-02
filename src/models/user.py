"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "users"

    email = db.Column(db.String(255))
    username = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255))

    def __init__(self, email, password, username=None):
        """ Create a new User """
        self.email = email
        from utils.mycrypt import hashstr, checkstr
        self.password = hashstr(password)
        self.username = username

    @classmethod
    def authenticate(cls, email, password):
        from utils.mycrypt import hashstr, checkstr
        user = cls.query.filter_by(email=email).first()
        return checkstr(user.password, password)
