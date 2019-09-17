from django.urls import include,path

from . import views

from . import forms



from courses.views import AboutView,CourseList,CourseDetails,CreateCourseView,UpdateCourseView,DeleteCourseView

urlpatterns = [

  path('about',AboutView.as_view()),

  path('',CourseList.as_view(), name='courses-list'),

  path('home',views.home),

  

  path('<int:course_id>/<int:step_id>', views.step_detail),

  path('<int:pk>/', views.detail),
  
  path('create',CreateCourseView.as_view(), name='courses-create'),


 path('update/<int:pk>/',UpdateCourseView.as_view(), name='courses-edit'),


 path('delete/<int:pk>/',DeleteCourseView.as_view(), name='courses-delete'),

 path('suggestion',views.suggestionView),



]