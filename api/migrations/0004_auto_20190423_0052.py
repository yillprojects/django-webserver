# Generated by Django 2.1.7 on 2019-04-22 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_residence_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='residence',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Residence'),
        ),
    ]
