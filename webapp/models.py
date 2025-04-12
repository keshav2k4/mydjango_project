from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Rollno = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    subject1 = models.CharField(max_length=30, default="Physics")
    subject2 = models.CharField(max_length=30, default="Maths")
    subject3 = models.CharField(max_length=30, default="Chemistry")

    def __str__(self):
        return self.Name


class Teacher(models.Model):
    Tid = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    Tname = models.CharField(max_length=30)
    Tsubject = models.CharField(max_length=30, default="Physics")

    def __str__(self):
        return self.Tname


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
