# Generated by Django 2.2 on 2019-05-31 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190531_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='tutorial_content',
            new_name='model_info',
        ),
    ]
