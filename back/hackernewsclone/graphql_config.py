from functools import lru_cache

import graphene
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django.types import DjangoObjectType

from hackernewsclone.forms import PostForm, WriterForm
from hackernewsclone.models import Post, Writer


class Connection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self.length


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        interfaces = (Node,)
        filter_fields = {"author__name": {"contains"}, "title": {"contains"}}
        connection_class = Connection


class WriterType(DjangoObjectType):
    class Meta:
        model = Writer
        interfaces = (Node,)
        filter_fields = {"name": {"contains"}}
        connection_class = Connection


class AddWriterMutation(DjangoModelFormMutation):
    writer = graphene.Field(WriterType)

    class Meta:
        form_class = WriterForm


class AddPostMutation(DjangoModelFormMutation):
    post = graphene.Field(PostType)

    class Meta:
        form_class = PostForm


class Mutations(graphene.ObjectType):
    add_writer = AddWriterMutation.Field()
    add_post = AddPostMutation.Field()


class Query(graphene.ObjectType):
    all_posts = DjangoFilterConnectionField(PostType)
    all_writers = DjangoFilterConnectionField(WriterType)
    post = Node.Field(PostType)
    writer = Node.Field(WriterType)


schema = graphene.Schema(query=Query, mutation=Mutations)
