# Generated by Django 4.0.1 on 2022-02-26 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_rename_name_userdata_name_of_party_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='date',
            new_name='Date',
        ),
    ]
