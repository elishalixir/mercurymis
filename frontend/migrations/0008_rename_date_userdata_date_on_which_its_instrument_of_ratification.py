# Generated by Django 4.0.1 on 2022-02-26 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_rename_date_userdata_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='Date',
            new_name='Date_on_which_its_instrument_of_ratification',
        ),
    ]
