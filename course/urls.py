# users/urls.py
from django.urls import path

from course.views.api import CourseListApiView

app_name = 'course'
urlpatterns = [
    path('', CourseListApiView.as_view(), name='course'),
]