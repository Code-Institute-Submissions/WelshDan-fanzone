# Generated by Django 3.2.23 on 2023-12-16 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supported', '0002_teamslist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamslist',
            name='league',
        ),
    ]
