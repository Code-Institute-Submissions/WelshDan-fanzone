# Generated by Django 3.2.23 on 2024-02-16 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supported', '0003_remove_teamslist_league'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Support',
        ),
    ]