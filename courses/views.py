from django.http import Http404
from django.shortcuts import render
from .models import Courses,Steps
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses}) 



def detail(request,course_id):
    try:
        course = Courses.objects.get(pk=course_id)
    except Courses.DoesNotExist:
        raise Http404("Courses does not exist")
    return render(request, 'courses/detail.html', {'course': course})

def step_detail(request,course_id,step_id):
    try:
        setp = Steps.objects.get(course_id=course_id, pk=step_id)
    except Courses.DoesNotExist:
        raise Http404("Courses does not exist")
    return render(request, 'courses/step_detail.html', {'setp': setp})




def home(request):
    return render(request, 'courses/layout/home.html') 

class AboutView(TemplateView):
    template_name = "courses/about.html"
    
