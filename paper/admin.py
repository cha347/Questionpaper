from django.contrib import admin
from paper.models import Course, Department
from django.db import models
from django.contrib import admin
from.models import*

# Register your models here.

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Question)
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','emailid','pwd')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject')

# iterable 
