# Generated by Django 4.2.9 on 2024-01-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
