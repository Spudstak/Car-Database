# Generated by Django 2.2 on 2019-05-31 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190531_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='tutorial_published',
            new_name='model_published',
        ),
    ]
