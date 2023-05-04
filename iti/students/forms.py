

from django import forms

""" create form based on the model"""
from students.models import  Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
