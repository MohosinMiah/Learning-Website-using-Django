from django.contrib import admin

from .models import Courses,Steps

# Register your models here.

        # TabularInline , StackedInline 
class SetpInline(admin.StackedInline):
    model = Steps


class CoursesAdmin(admin.ModelAdmin):
    inlines = [SetpInline,]


admin.site.register(Courses,CoursesAdmin)
admin.site.register(Steps)