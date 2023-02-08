from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student_list',views.student_list,name='student_list'),
    path('student_list_using_datatables.net',views.student_list_using_datatables,name='student_list_using_datatables'),
    path('csv_download',views.csv_download,name='csv_download'),
    path('generate_students',views.generate_students,name='generate_students')
    
]
