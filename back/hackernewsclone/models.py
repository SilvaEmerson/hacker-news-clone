from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Writer(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Writer[name={self.name}]"


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Writer, on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"Post[title={self.title}, author={self.author.name}]"


@receiver(post_save, sender=Post)
def handle_new_post(*args, **kwargs):
    print(args)
    print(kwargs)
