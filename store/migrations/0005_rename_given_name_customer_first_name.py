# Generated by Django 3.2.4 on 2023-12-13 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_first_name_to_given_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='given_name',
            new_name='first_name',
        ),
    ]
