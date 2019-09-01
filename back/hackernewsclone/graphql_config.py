import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django.types import DjangoObjectType

from hackernewsclone.models import Post, Writer
from hackernewsclone.forms import PostForm, WriterForm


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class WriterType(DjangoObjectType):
    class Meta:
        model = Writer


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
    all_posts = graphene.List(PostType)
    all_writers = graphene.List(WriterType)
    get_posts = graphene.List(
        PostType, title=graphene.String(), author=graphene.String()
    )
    get_post = graphene.Field(PostType, id=graphene.Int())

    def resolve_all_writers(self, info, **kwargs):
        return Writer.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.select_related("author").all()

    def resolve_get_posts(self, info, **kwargs):
        title = kwargs.get("title", None)
        author = kwargs.get("author", None)

        if author:
            return Post.objects.select_related("author").filter(
                author__name=author
            )

        if title:
            return Post.objects.filter(title__contains=title)

    def resolve_get_post(self, info, **kwargs):
        return Post.objects.get(pk=kwargs.get("id", None))


schema = graphene.Schema(query=Query, mutation=Mutations)
