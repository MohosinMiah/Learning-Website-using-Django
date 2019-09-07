from django.urls import include,path

from . import views

urlpatterns = [

    path('',views.index),

    path('home',views.home),

    path('<int:course_id>', views.detail),

  path('<int:course_id>/<int:step_id>', views.step_detail),



]