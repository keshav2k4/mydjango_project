# webapp/models.py
from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Rollno = models.IntegerField( validators=[MinValueValidator(1)], null=True)  # Allow null for now
    subject1 = models.CharField(max_length=30,default="Physics")
    subject2 = models.CharField(max_length=30,default="Maths")
    subject3 = models.CharField(max_length=30,default="Chemistry")


    def __str__(self):
        return self.Name
