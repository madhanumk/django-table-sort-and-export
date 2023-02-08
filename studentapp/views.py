from django.shortcuts import render
from .models import Student, State, Grade
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'home.html')


def student_list(request):   
    order = request.GET.get('order')
    field = request.GET.get('field')
    export = request.GET.get('export')
    page = request.GET.get('page',1)
    if field is None:
        field = "name"
    if order is None:
        order = "ASC"

    if order == "ASC":
        student_list = Student.objects.all().order_by(field)
    else:
        student_list = Student.objects.all().order_by('-'+str(field))

    if export == "yes":
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="student_list.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Roll No', 'Gender', 'Age','Grade','Section','State','Country'])

        students = student_list.values_list('name', 'roll_no', 'gender', 'age','grade__name','section','state__name','state__country__name')
        for student in students:
            writer.writerow(student)
        return response

    paginator = Paginator(student_list, 20)

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    context = {
        'students' : students,
        'order' : order,
        'field' : field,
    }
    return render(request, 'students_list.html', context)


def student_list_using_datatables(request):  
    students = Student.objects.all()
    context = {
        'students' : students,      
    }
    return render(request, 'students_list_datatables.html', context)

def csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_list.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Roll No', 'Gender', 'Age','Grade','Section','State','Country'])
    students = Student.objects.all().values_list('name', 'roll_no', 'gender', 'age','grade__name','section','state__name','state__country__name')
    for student in students:
        writer.writerow(student)

    return response


def generate_students(request):
    state = State.objects.order_by('?').first()
    grade = Grade.objects.order_by('?').first()
    for i in range(1,10000):
        Student.objects.create(name="Student "+str(i),roll_no="24HG"+str(i),age=19,gender='M',state=state,grade=grade,section="A")
    return HttpResponse("Done")