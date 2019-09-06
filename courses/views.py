from django.http import Http404
from django.shortcuts import render
from .models import Courses
# Create your views here.

def index(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses}) 


    
def home(request):
    return render(request, 'courses/layout/home.html') 