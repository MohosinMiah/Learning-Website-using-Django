from django.urls import include,path

from . import views



from courses.views import AboutView,CourseList,CourseDetails,CreateCourseView

urlpatterns = [

  path('about',AboutView.as_view()),

  path('',CourseList.as_view(), name='courses-list'),

  path('home',views.home),

  

  path('<int:course_id>/<int:step_id>', views.step_detail),

  path('<int:pk>/', CourseDetails.as_view()),
  
  path('create',CreateCourseView.as_view()),


]