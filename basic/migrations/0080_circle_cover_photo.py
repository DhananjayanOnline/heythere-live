# Generated by Django 4.0.5 on 2022-08-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0079_alter_userregister_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
