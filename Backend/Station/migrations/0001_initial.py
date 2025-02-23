# Generated by Django 5.1.6 on 2025-02-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationName', models.CharField(max_length=255)),
                ('trainLine', models.CharField(max_length=255)),
                ('leftETA', models.IntegerField()),
                ('rightETA', models.IntegerField()),
                ('leftCurrentDensity', models.CharField(max_length=255)),
                ('rightCurrentDensity', models.CharField(max_length=255)),
                ('leftHistory', models.CharField(max_length=255)),
                ('rightHistory', models.CharField(max_length=255)),
                ('cctv', models.CharField(max_length=255)),
                ('isOperating', models.BooleanField(default=True)),
                ('stationIMG', models.CharField(max_length=255)),
            ],
        ),
    ]
