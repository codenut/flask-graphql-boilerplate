import graphene
from .user_schema import UserQuery, CreateUser
from .auth_schema import CreateAuth


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_auth = CreateAuth.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
