# Generated by Django 4.0.5 on 2022-08-19 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0075_alter_userregister_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='cover_photo',
            field=models.ImageField(blank=True, default='hero/banner-img.jpg', null=True, upload_to=''),
        ),
    ]
