# Generated by Django 3.1.3 on 2021-01-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0036_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.DeleteModel(
            name='chat_first_question_model',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]
