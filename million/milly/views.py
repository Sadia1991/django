from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render
from .models import Student

import names


# Create your views here.

def myview(request):
    # Iterate through all the data items

    insert_list = []

    for i in range(100):
        name = names.get_full_name()
        insert_list.append(Student(student_name=name))
    Student.objects.bulk_create(insert_list)
    # Insert in the database
    # Student.objects.bulk_create([Student(student_name=names.get_full_name())])

    # Getting all the stuff from database
    query_results = Student.objects.all()[:10]

    # Creating a dictionary to pass as an argument
    context = {'query_results': query_results}

    # Returning the rendered html
    return render(request, "home.html", context)


def myedit(request):
    id_tuple = [606919, 606920, 606921]
    for i in id_tuple:
        Student.objects.get(id=i).update(student_name=Concat('student_name', Value('-updated')))

    student_query = Student.objects.all()[:10]

    stu_text = {'student_query': student_query}

    return render(request, "home.html", stu_text)
