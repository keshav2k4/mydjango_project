from django.contrib import admin
from django.urls import path, include
from webapp import views  # Import views from the webapp app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register_teacher, name='home'),  # Add this line to direct the root to the view_students page
    path('add_student/', views.add_student, name='add_student'),
    path('view_students/', views.view_students, name='view_students'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
]
