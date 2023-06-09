# Generated by Django 3.2.19 on 2023-05-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, error_messages={'unique': 'This title already exists. Use search bar to find the post'}, max_length=255, unique=True),
        ),
    ]
