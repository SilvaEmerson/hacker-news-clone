# Generated by Django 2.2.4 on 2019-09-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hackernewsclone", "0003_auto_20190901_0257")]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name="writer",
            name="name",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
