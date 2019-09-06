from django.db import models

# Create your models here.

#Courses Table Create

class Courses(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title





class Steps(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)

    def __str__(self):
        return self.title