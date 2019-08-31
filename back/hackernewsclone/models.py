from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=250)

    def __repr__(self):
        return f"Writer[name={self.name}]"


class Post(models.Model):
    title = models.CharField(max_length=250)
    writer = models.OneToOneField(Writer, on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"Post[title={self.title}]"

