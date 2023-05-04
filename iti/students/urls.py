"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
# from students.views import helloworld
import  students.views
from students.views import  allstudents, getstudent, \
    landingpage, studnets_list, students_index, student_delete, \
    student_show, create_student, edit_student
urlpatterns = [

    path('hello',students.views.helloworld
         , name='helloworld'),
    path('alll',allstudents
         , name='allstudents'),

    path('<int:id>',getstudent
         , name='getstudent'),

    path('land',landingpage, name='landing'),
    path('list',studnets_list, name='students_list' ),
    path('index', students_index, name='students.index'),
    path('index/<int:id>/delete', student_delete, name='students.delete'),
    path('index/<int:id>', student_show, name='students.show'),
    path('create', create_student, name='students.create'),
    path('index/<int:id>/edit', edit_student, name='students.edit'),
]