from models import User as UserModel
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )


class UserQuery(graphene.ObjectType):
    user = graphene.List(User, email=graphene.String())

    def resolve_user(self, info, email):
        query = User.get_query(info)
        return query.filter_by(email=email)


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()

    def mutate(self, info, email, password, username=None):
        user = UserModel(username=username, email=email, password=password)
        user.save()
        ok = True
        return CreateUser(user=user, ok=ok)
