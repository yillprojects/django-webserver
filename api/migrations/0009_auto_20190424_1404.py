# Generated by Django 2.1.7 on 2019-04-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190424_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars'),
        ),
    ]
