# Generated by Django 4.2 on 2023-04-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='items',
            field=models.ManyToManyField(to='main_app.item'),
        ),
    ]