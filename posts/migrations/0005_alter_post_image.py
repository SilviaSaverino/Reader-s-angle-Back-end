# Generated by Django 3.2.19 on 2023-05-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='../default_book_q79btx', upload_to='images/'),
        ),
    ]
