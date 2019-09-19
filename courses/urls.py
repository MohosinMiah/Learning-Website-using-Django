from django.urls import include,path

from . import views

from . import forms



from courses.views import AboutView,CourseList,CourseDetails,CreateCourseView,UpdateCourseView,DeleteCourseView

urlpatterns = [

  path('about',AboutView.as_view()),

  path('',CourseList.as_view(), name='courses-list'),

  path('home',views.home),

  
path('<int:pk>/', views.detail),

  path('<int:course_id>/t<int:step_id>', views.text_detail,name='text_detail'),

  path('<int:course_id>/q<int:step_id>', views.quiz_detail,name='quiz_detail'),


  
  
  path('create',CreateCourseView.as_view(), name='courses-create'),


 path('update/<int:pk>/',UpdateCourseView.as_view(), name='courses-edit'),


 path('delete/<int:pk>/',DeleteCourseView.as_view(), name='courses-delete'),

 path('suggestion',views.suggestionView),

 path('<int:course_id>/create/quiz',views.quiz_create,name="create_quiz"),


  path('<int:course_id>/edit/quiz/<int:quiz_id>',views.quiz_edit,name="edit_quiz"),




]