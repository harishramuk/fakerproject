# Generated by Django 3.0.11 on 2020-12-26 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0002_banglorejobs_hydjobs_punejobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chennaijobs',
            new_name='Banglorejob',
        ),
        migrations.RenameModel(
            old_name='Hydjobs',
            new_name='Chennaijob',
        ),
        migrations.RenameModel(
            old_name='Punejobs',
            new_name='Hydjob',
        ),
        migrations.RenameModel(
            old_name='Banglorejobs',
            new_name='Punejob',
        ),
    ]
