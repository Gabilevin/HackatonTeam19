# Generated by Django 3.1.3 on 2021-01-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20210106_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]