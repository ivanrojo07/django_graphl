import graphene
from tag.graphql.input import TagInput

class ArticleInput(graphene.InputObjectType):
    id = graphene.ID()
    author = graphene.ID()
    title = graphene.String()
    body = graphene.String()
    tags = graphene.List(TagInput)
    category = graphene.ID()