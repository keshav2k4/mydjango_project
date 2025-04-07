# student_app/views.py
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'student_app/add_student.html', {'form': form})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'student_app/view_students.html', {'students': students})
