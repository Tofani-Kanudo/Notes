# Generated by Django 2.2 on 2019-04-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_todotime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todotime',
            name='time',
        ),
    ]