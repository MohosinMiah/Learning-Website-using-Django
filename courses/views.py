from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    courses = ("PHP ","JAVA "," PYTHON")
    return HttpResponse(courses)