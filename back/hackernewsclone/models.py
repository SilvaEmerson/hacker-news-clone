import json

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from hackernewsclone.signals import send_channel_message


class Post(models.Model):
    class Meta:
        unique_together = ("title", "author")

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1000)

    def __repr__(self):
        return f"Post[title={self.title}, author={self.author.name}]"


@receiver(post_save, sender=Post)
def handle_new_post(*args, **kwargs):
    instance = kwargs["instance"]
    message = {"title": instance.title, "author": instance.author.username}
    send_channel_message(instance.author.username, message)
