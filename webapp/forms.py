# student_app/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Name', 'Rollno', 'subject1', 'subject2', 'subject3']
