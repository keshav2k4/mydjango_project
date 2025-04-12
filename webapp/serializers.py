# webapp/serializers.py
from rest_framework import serializers
from .models import Student, Teacher, Subject, Marks

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'Name', 'Rollno', 'subject1', 'subject2', 'subject3']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['Tid', 'Tname', 'Tsubject']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class MarksSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Nested student data
    subject = SubjectSerializer()  # Nested subject data

    class Meta:
        model = Marks
        fields = ['id', 'student', 'subject', 'marks']
