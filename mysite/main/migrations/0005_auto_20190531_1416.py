# Generated by Django 2.2 on 2019-05-31 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190531_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='tutorial_series',
            new_name='car_manufacturer',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='tutorial_series',
            new_name='car_manufacturer',
        ),
    ]