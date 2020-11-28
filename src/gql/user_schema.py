from models import User as UserModel
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)


class UserQuery(graphene.ObjectType):
    user = graphene.List(User, username=graphene.String())

    def resolve_user(self, info, username):
        query = User.get_query(info)
        return query.filter_by(username=username)


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()

    def mutate(self, info, username, email):

        user = UserModel(username=username, email=email)
        user.save()
        ok = True
        return CreateUser(user=user, ok=ok)
