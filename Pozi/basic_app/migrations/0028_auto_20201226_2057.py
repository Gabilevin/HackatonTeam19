# Generated by Django 3.1.3 on 2020-12-26 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0027_chat_first_question_model_fell'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat_first_question_model',
            old_name='fell',
            new_name='feel',
        ),
    ]