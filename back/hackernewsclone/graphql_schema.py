import graphene
from graphene_django.types import DjangoObjectType

from hackernewsclone.models import Post, Writer


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class WriterType(DjangoObjectType):
    class Meta:
        model = Writer


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_writers = graphene.List(WriterType)
    get_posts = graphene.List(PostType, title=graphene.String(), writer=graphene.String())
    get_post = graphene.Field(PostType, id=graphene.Int())

    def resolve_all_writers(self, info, **kwargs):
        return Writer.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.select_related('writer').all()

    def resolve_get_posts(self, info, **kwargs):
        title = kwargs.get('title', None)
        writer = kwargs.get('writer', None)
        
        if writer:
            return Post.objects.select_related('writer').filter(writer__name=writer)

        if title:
            return Post.objects.filter(title__contains=title)

    def resolve_get_post(self, info, **kwargs):
        return Post.objects.get(pk=kwargs.get('id', None)) 


schema = graphene.Schema(
    query=Query
)
