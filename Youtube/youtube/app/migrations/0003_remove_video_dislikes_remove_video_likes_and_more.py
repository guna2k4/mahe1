# Generated by Django 5.0.3 on 2024-03-09 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='view',
        ),
    ]