from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Courses,Steps
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.conf import settings
# Create your views here.

# Function Based DIsplay List 

def index(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses}) 

# Class Base Display ListView 

class CourseList(CreateView,ListView):

    context_object_name = "courses"

    model = Courses

    fields = ['title','description']

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
        # def get_object(self):
        #     id = self.kwargs.get('pk')
        #     return get_object_or_404(Courses, pk=id)

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

class SuggestionView(TemplateView):
    template_name = "courses/suggestion.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.SuggesstionForm()
        return context

    
class CreateCourseView(CreateView):
    model = Courses
    fields = ["title","description",]


    
class UpdateCourseView(LoginRequiredMixin,UpdateView):
    model = Courses
    template_name = "courses/update_form.html"

    fields = ["title","description",]

class DeleteCourseView(LoginRequiredMixin,DeleteView):
    model = Courses



    success_url = reverse_lazy('courses-list')   

    def get_login_url(self):
        """
        Override this method to override the login_url attribute.
        """
        # login_url = self.login_url or settings.LOGIN_URL
        # if not login_url:
        #     raise ImproperlyConfigured(
        #         '{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL, or override '
        #         '{0}.get_login_url().'.format(self.__class__.__name__)
        #     )
        return str("/admin/login/?next=/admin/")

# Before User Check User Status 
    # def get_queryset(self):
    #     if not self.request.user.is_superuser:
    #         return self.model.objects.filter(coach=self.request.user)
    #     return self.model.objects.all()    



