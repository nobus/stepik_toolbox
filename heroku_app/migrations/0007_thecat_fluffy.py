# Generated by Django 3.0.4 on 2020-05-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroku_app', '0006_auto_20200415_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='thecat',
            name='fluffy',
            field=models.BooleanField(default=True),
        ),
    ]