# Generated by Django 5.1.6 on 2025-03-08 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Station', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='cctv',
        ),
        migrations.RemoveField(
            model_name='station',
            name='leftHistory',
        ),
        migrations.RemoveField(
            model_name='station',
            name='rightHistory',
        ),
        migrations.AddField(
            model_name='station',
            name='leftCCTV',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='rightCCTV',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='leftCurrentDensity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='leftETA',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='rightCurrentDensity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='rightETA',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='DailyDensity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('leftDensity', models.CharField(max_length=255, null=True)),
                ('rightDensity', models.CharField(max_length=255, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Station.station')),
            ],
        ),
        migrations.CreateModel(
            name='HourlyDensity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('leftDensity', models.CharField(max_length=255, null=True)),
                ('rightDensity', models.CharField(max_length=255, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Station.station')),
            ],
        ),
    ]
