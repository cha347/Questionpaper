# Generated by Django 3.2.4 on 2021-09-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0011_remove_question_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Course',
            field=models.CharField(choices=[('Btech in Computer Science', 'Btech in Computer Science'), ('Btech in Mechanical', 'Btech in Mechanical'), ('law ', 'law')], max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='Department',
            field=models.CharField(choices=[('Department of BBA', 'Department of BBA'), ('Department of Engineering', 'Department of Engineering'), ('Department of Commerce', 'Department of Commerce')], max_length=50),
        ),
    ]
