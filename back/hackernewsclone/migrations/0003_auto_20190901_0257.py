# Generated by Django 2.2.4 on 2019-09-01 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("hackernewsclone", "0002_auto_20190831_1211")]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hackernewsclone.Writer",
            ),
        )
    ]
