# Generated by Django 3.2.23 on 2024-02-13 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_filter',
        ),
    ]
