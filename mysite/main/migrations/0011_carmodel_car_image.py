# Generated by Django 2.2 on 2019-06-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190603_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]