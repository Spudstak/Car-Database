# Generated by Django 2.2 on 2019-05-31 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190531_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='tutorial_title',
            new_name='model_title',
        ),
    ]
