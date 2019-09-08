from django.test import TestCase

from .models import Courses

from django.utils import timezone


# Create your tests here.


class CoursesModelTests(TestCase):
    def test_course_creation(self):
        course = Courses.objects.create(
            title ="How to Test Model in django",
            description ="Discussed details all in one "
        )

        now = timezone.now()

        self.assertLessEqual(course.created_at,now)



