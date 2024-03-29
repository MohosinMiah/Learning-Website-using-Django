from django.contrib import admin

from .models import Courses,Text,Quizs,Question,Answer,MultipleChoiseQuestion,TrueFalseQuestion

# Register your models here.

        # TabularInline , StackedInline 
        
class TextInline(admin.StackedInline):
    model = Text


class CoursesAdmin(admin.ModelAdmin):
    inlines = [TextInline,]
    


admin.site.register(Courses,CoursesAdmin)
admin.site.register(Text)

admin.site.register(Quizs)

admin.site.register(MultipleChoiseQuestion)
admin.site.register(TrueFalseQuestion)


admin.site.register(Answer)

