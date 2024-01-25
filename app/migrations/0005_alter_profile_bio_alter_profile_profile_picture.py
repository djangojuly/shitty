# Generated by Django 5.0.1 on 2024-01-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='media/user.png', upload_to='media'),
        ),
    ]
