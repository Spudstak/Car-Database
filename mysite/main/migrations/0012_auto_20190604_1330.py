# Generated by Django 2.2 on 2019-06-04 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_carmodel_car_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='car_image',
            new_name='model_image',
        ),
    ]
