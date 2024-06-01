# Generated by Django 5.0.6 on 2024-06-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_hotel_info_faxnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_info',
            name='faxnumber',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='hotelcode',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='hotelname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='hotelrating',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='map',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='phonenumber',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='pincode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]