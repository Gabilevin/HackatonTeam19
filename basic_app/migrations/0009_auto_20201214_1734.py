# Generated by Django 3.1.3 on 2020-12-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20201214_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
