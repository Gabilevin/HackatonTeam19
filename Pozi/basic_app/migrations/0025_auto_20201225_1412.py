# Generated by Django 3.1.3 on 2020-12-25 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0024_auto_20201225_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motivation',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='stand_up',
            name='subject',
        ),
    ]