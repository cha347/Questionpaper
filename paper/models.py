from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models her


  
    
class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Course(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
SEM_CHOICES =( 
   ('Sem1','Sem1'),
     ('Sem2','Sem2'),
       ('Sem3','Sem3'),

) 
DEPARTMENT_CHOICES=(
    ('Department of BBA','Department of BBA'),
   ( 'Department of Engineering','Department of Engineering'),
   ('Department of Commerce','Department of Commerce'),
)
COURSE_CHOICES=(
    ('Btech in Computer Science','Btech in Computer Science'),
    ( 'Btech in Mechanical','Btech in Mechanical'),
    ('law ','law')


)
YEAR_CHOICES=(
    ('2019','2019'),
    ('2018','2018')
)

class Question(models.Model):
    
    Department=models.CharField(max_length=50,choices=DEPARTMENT_CHOICES)
    Course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    

    Semester=models.CharField(max_length=50,choices=SEM_CHOICES)
    
    my_file=models.FileField(upload_to='doc',blank=True)

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    def __str__(self):
        return self.name