from models import User as UserModel
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene


class Auth(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node, )


class CreateAuth(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, email, password, username=None):
        ok = UserModel.authenticate(email, password)
        return CreateAuth(ok=ok)
