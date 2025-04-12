from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm
from .models import Student, Teacher
from rest_framework import viewsets
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
def add_student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'student_app/add_student.html', {'form': form})

# View All Students
def view_students(request):
    students = Student.objects.all()
    return render(request, 'student_app/view_students.html', {'students': students})

# Register Teacher View
def register_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()  # Save teacher to database
            return redirect('teacher_list')  # Redirect to the teacher list page
    else:
        form = TeacherForm()
    return render(request, 'student_app/register_teacher.html', {'form': form})

# List All Teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'student_app/teacher_list.html', {'teachers': teachers})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    