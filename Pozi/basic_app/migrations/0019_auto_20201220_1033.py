# Generated by Django 3.1.3 on 2020-12-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0018_auto_20201219_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='tip_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('text', models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='activation',
            name='user',
        ),
        migrations.DeleteModel(
            name='regiter_all',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Activation',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]