# Generated by Django 3.2.8 on 2021-11-13 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child_app', '0002_auto_20211113_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='idParent',
            new_name='parent',
        ),
    ]