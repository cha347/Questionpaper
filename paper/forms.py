from django import forms
from django.forms import ModelForm

# creating a form  
from .models import Question
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['Department','Course','Semester','my_file']
        widgets={'Department':forms.TextInput(attrs={'class':'form-control'}),
        'Course':forms.TextInput(attrs={'class':'form-control'}),
        'Semester':forms.TextInput(attrs={'class':'form-control'}),
        }


    