# Generated by Django 3.1.3 on 2021-01-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20210106_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='aproved',
        ),
        migrations.AddField(
            model_name='chat_first_question_model',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]