# Generated by Django 3.0.4 on 2020-04-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroku_app', '0003_thecat_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thecat',
            name='avatar',
            field=models.ImageField(upload_to='avatars'),
        ),
    ]