# Generated by Django 3.1.3 on 2020-12-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0021_qa_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='stand_up',
            name='video1',
            field=models.URLField(null=True),
        ),
    ]
