import graphene
from article.graphql.type import ArticleType
from article.graphql.resolvers import resolve_get_articles, resolve_get_article

class Query(graphene.ObjectType):
    get_articles = graphene.List(ArticleType)
    get_article = graphene.Field(ArticleType, id = graphene.Int())

    def resolve_get_articles(self, info, **kwargs):
        return resolve_get_articles(info, **kwargs)

    def resolve_get_article(self, info, **kwargs):
        return resolve_get_article(info, **kwargs)