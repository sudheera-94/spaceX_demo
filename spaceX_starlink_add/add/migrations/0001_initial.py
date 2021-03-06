# Generated by Django 3.1.4 on 2020-12-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('satelliteId', models.IntegerField(primary_key=True, serialize=False)),
                ('satelliteName', models.CharField(blank=True, max_length=20)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('healthPercentage', models.IntegerField(blank=True, default=100)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('xCoordinate', models.IntegerField(blank=True)),
                ('yCoordinate', models.IntegerField(blank=True)),
                ('xVelocity', models.IntegerField(blank=True, default=0)),
                ('yVelocity', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
