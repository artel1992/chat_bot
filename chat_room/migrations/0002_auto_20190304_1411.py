# Generated by Django 2.1.7 on 2019-03-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='dat',
            new_name='data',
        ),
    ]