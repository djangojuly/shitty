# Generated by Django 5.0.1 on 2024-01-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_profile_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Hey There I am using ShittyMessenger', max_length=200, null=True),
        ),
    ]
