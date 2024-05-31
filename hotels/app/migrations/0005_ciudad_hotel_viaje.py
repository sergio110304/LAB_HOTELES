# Generated by Django 5.0.6 on 2024-05-31 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_countrycode_pais_countrycode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('citycode', models.CharField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(max_length=50)),
                ('countrycode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotelcode', models.CharField(primary_key=True, serialize=False)),
                ('hotelname', models.CharField(max_length=50)),
                ('hotelrating', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('attractions', models.TextField()),
                ('faxnumber', models.CharField(max_length=50)),
                ('hotelfacilities', models.TextField()),
                ('map', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=50)),
                ('hotelwebsiteurl', models.CharField(max_length=200)),
                ('citycode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('idviaje', models.CharField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('hotelcode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.hotel')),
                ('idusuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.usuario')),
            ],
        ),
    ]
