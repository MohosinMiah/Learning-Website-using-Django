from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Courses,Steps

from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views import generic


# Create your views here.

# Function Based DIsplay List 

def index(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses}) 

# Class Base Display ListView 

class CourseList(ListView):

    context_object_name = "courses"

    model = Courses

    template_name = "courses/course_list.html"


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['courses']  = Courses.objects.all()

    #     return context


class CourseDetails(DetailView):
        model = Courses

        context_object_name = "course"

        # template_name = "courses/courses_detail.html"


        # We Also Can flow THis Method   
        def get_object(self):
            id = self.kwargs.get('pk')
            return get_object_or_404(Courses, pk=id)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_books'] = 6
        return context
    
class CreateCourseView(CreateView):
    model = Courses
    fields = ["title","description",]


