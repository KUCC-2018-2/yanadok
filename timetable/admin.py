from django.contrib import admin
from .models import Timetable
from course.models import Course

# Register your models here.
admin.site.register(Course)
admin.site.register(Timetable)