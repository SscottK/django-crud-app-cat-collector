# Generated by Django 4.2.16 on 2024-11-08 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
