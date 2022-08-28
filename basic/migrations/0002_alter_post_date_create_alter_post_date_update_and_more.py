# Generated by Django 4.0.5 on 2022-06-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='downvote',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvote',
            field=models.IntegerField(null=True),
        ),
    ]
