# Generated by Django 4.0.5 on 2022-07-17 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0060_alter_circle_options_circle_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='circle_visibility',
        ),
    ]