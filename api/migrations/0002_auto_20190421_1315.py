# Generated by Django 2.1.7 on 2019-04-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country')),
                ('region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='residence',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Residence'),
        ),
    ]
