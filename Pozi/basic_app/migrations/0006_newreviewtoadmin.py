# Generated by Django 3.1.3 on 2020-12-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20201207_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewReviewToAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reviews', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]