# Generated by Django 2.2 on 2019-05-30 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartype',
            old_name='tutorial_category',
            new_name='car_category',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='tutorial_category',
            new_name='car_category',
        ),
    ]
