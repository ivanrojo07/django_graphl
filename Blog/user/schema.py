import graphene
from user.graphql.query import Query
from user.graphql.mutations import CreateUser, UpdateUser, DeleteUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)