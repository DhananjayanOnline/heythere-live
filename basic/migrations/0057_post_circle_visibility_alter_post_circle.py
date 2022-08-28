# Generated by Django 4.0.5 on 2022-07-14 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0056_alter_post_circle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='circle_visibility',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='circle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='circle', to='basic.circle'),
        ),
    ]