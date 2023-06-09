# Generated by Django 3.2.19 on 2023-05-24 13:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_alter_post_title'),
        ('post_followers', '0004_alter_postfollower_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postfollower',
            old_name='post',
            new_name='followed_post',
        ),
        migrations.AlterUniqueTogether(
            name='postfollower',
            unique_together={('owner', 'followed_post')},
        ),
    ]
