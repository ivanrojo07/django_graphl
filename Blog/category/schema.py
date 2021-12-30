import graphene
from category.graphql.query import Query
from category.graphql.mutations import CreateCategory, UpdateCategory, DeleteCategory

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)