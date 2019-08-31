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
    post = graphene.Field(PostType, id=graphene.Int(), title=graphene.String())

    def resolve_all_writers(self, info, **kwargs):
        return Writer.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.select_related('writer').all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id', None)
        title = kwargs.get('title', None)
        writer = kwargs.get('writer', None)
        
        if writer:
            return Post.objects.select_related('writer').get(name=writer)

        if title:
            return Post.objects.select_related('title').get(name=writer)

        if id:
            return Post.objects.select_related('id').get(name=writer)

schema = graphene.Schema(
    query=Query
)
