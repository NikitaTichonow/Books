# Generated by Django 5.0.3 on 2024-04-29 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookInstance',
            new_name='BookStatus',
        ),
    ]