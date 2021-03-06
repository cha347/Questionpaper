# Generated by Django 3.2.4 on 2021-09-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_auto_20210901_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(choices=[('Department of BBA', 'Department of BBA'), ('Department of Engineering', 'Department of Engineering')], max_length=50)),
                ('Course', models.CharField(choices=[('Btech in Computer Science', 'Btech in Computer Science'), ('Btech in Mechanical', 'Btech in Mechanical')], max_length=50)),
                ('Year', models.PositiveIntegerField(choices=[('2019', '2019'), ('2018', '2018')])),
                ('Semester', models.CharField(choices=[('Sem1', 'Sem1'), ('Sem2', 'Sem2'), ('Sem3', 'Sem3')], max_length=50)),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
