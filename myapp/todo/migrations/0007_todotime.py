# Generated by Django 2.2 on 2019-04-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_delete_todotime'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
