# Generated by Django 4.0.1 on 2022-02-26 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_userdata_part_a'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='name',
            new_name='Name_of_party',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='Part_A',
        ),
    ]
