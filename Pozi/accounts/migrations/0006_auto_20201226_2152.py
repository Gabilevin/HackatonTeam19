# Generated by Django 3.1.3 on 2020-12-26 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201226_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regiter_extra_model',
            old_name='User',
            new_name='user',
        ),
    ]