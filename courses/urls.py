from django.urls import include,path

from . import views
from courses.views import AboutView

urlpatterns = [
    path('about', AboutView.as_view()),

    path('',views.index),

    path('home',views.home),

    path('<int:course_id>', views.detail),

  path('<int:course_id>/<int:step_id>', views.step_detail),



]