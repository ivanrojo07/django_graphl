import graphene
import graphql_jwt
import tag.schema
import user.schema
import category.schema
import article.schema

class Query(category.schema.Query, article.schema.Query, user.schema.Query, tag.schema.Query, graphene.ObjectType):
    pass

class Mutation( category.schema.Mutation, article.schema.Mutation, user.schema.Mutation, tag.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field() #give json web toke if credentials are correct
    verify_token = graphql_jwt.Verify.Field()   #we use this token to verify our jwt
    refresh_token = graphql_jwt.Refresh.Field() #refresh our jwt


schema = graphene.Schema(query=Query, mutation=Mutation)