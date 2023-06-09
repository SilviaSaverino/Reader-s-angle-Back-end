# Generated by Django 3.2.19 on 2023-05-27 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_image'),
        ('poststatus', '0006_alter_poststatus_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poststatus',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='status_choice', to='profiles.profile'),
        ),
    ]
