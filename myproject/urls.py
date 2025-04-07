# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from webapp import views  # Make sure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/add/', views.add_student, name='add_student'),
    path('students/view/', views.view_students, name='view_students'),
    path('', views.view_students, name='home'),  # Redirect root URL to 'view_students'
]
