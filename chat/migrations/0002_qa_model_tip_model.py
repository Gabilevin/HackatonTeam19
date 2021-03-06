# Generated by Django 3.1.3 on 2021-01-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QA_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('text', models.TextField(max_length=5000, null=True)),
                ('release_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tip_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('text', models.TextField(max_length=5000, null=True)),
                ('release_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
