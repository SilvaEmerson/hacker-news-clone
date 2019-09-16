from functools import lru_cache

import graphene
import graphql_jwt
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User

from hackernewsclone.forms import PostForm, UserForm
from hackernewsclone.models import Post


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
        filter_fields = {"author__username": {"contains"}, "title": {"contains"}}
        connection_class = Connection


class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node,)
        filter_fields = {"username": {"contains"}}
        connection_class = Connection


class AddUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UserForm


class AddPostMutation(DjangoModelFormMutation):
    post = graphene.Field(PostType)

    class Meta:
        form_class = PostForm


class Mutations(graphene.ObjectType):
    add_user = AddUserMutation.Field()
    add_post = AddPostMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(graphene.ObjectType):
    all_posts = DjangoFilterConnectionField(PostType)
    all_writers = DjangoFilterConnectionField(UserType)
    post = Node.Field(PostType)
    user = Node.Field(UserType)


schema = graphene.Schema(query=Query, mutation=Mutations)
