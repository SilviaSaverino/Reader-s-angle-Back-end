# Generated by Django 3.2.19 on 2023-05-17 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('author', models.CharField(blank=True, max_length=255)),
                ('genre', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='../default_book_w68xtp', upload_to='images/')),
                ('image_filter', models.CharField(choices=[('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'), ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'), ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'), ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'), ('walden', 'Walden'), ('xpro2', 'X-pro II')], default='normal', max_length=30)),
                ('genre_filter', models.CharField(choices=[('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction'), ('mystery', 'Mystery'), ('fantasy', 'Fantasy'), ('romance', 'Romance'), ('thriller', 'Thriller'), ('biography', 'Biography'), ('poetry', 'Poetry'), ('children', 'Children'), ('cookbooks', 'Cookbooks')], default='normal', max_length=30)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
