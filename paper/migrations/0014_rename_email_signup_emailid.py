# Generated by Django 3.2.4 on 2021-09-03 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0013_auto_20210903_0642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='email',
            new_name='emailid',
        ),
    ]
