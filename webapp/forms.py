from django import forms
from .models import Student, Teacher

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Name', 'Rollno', 'subject1', 'subject2', 'subject3']

# Teacher Form
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['Tid', 'Tname', 'Tsubject']
        
