from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def student_list(response):
    students = Student.objects.all()
    text = ""
    for student in students:
        text += f"{student.fisrt_name} {student.last_name} <br>"
        print(student.fisrt_name)

    return HttpResponse(text)