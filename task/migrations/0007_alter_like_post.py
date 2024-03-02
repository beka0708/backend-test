# Generated by Django 5.0.2 on 2024-03-02 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0006_rename_publication_like_post_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes",
                to="task.post",
            ),
        ),
    ]
