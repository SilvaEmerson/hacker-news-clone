# Generated by Django 2.2.4 on 2019-09-09 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("hackernewsclone", "0005_auto_20190909_1518")]

    operations = [
        migrations.AlterUniqueTogether(
            name="post", unique_together={("title", "author")}
        )
    ]