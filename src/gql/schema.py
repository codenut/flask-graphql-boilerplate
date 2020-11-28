import graphene
from .user_schema import UserQuery, CreateUser


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
