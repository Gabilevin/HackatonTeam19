# Generated by Django 3.1.3 on 2020-12-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201220_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiter_extra_model',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='regiter_extra_model',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
