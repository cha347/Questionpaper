# Generated by Django 3.2.4 on 2021-09-01 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0008_rename_questions_answers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Question',
        ),
    ]
