from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students(request):
    students = [
        {"Id":"Anit","Dis":"I am 25 year old"}
    ]
    return HttpResponse(students)
