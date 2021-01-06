# Generated by Django 3.1.3 on 2020-12-28 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_auto_20201227_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiter_extra_model',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regiter_extra_model', to=settings.AUTH_USER_MODEL),
        ),
    ]