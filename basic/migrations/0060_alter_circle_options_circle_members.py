# Generated by Django 4.0.5 on 2022-07-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0059_circle_neighbourhood'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circle',
            options={'ordering': ['-date_create']},
        ),
        migrations.AddField(
            model_name='circle',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members', to='basic.userregister'),
        ),
    ]
