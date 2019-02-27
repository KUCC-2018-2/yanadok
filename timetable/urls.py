from django.urls import path

from course.views.api import CourseListApiView
from timetable.views.api import TimetableApiView
from timetable.views.timetable import TimetableView, UpdateTimetableView

app_name = 'timetable'
urlpatterns = [
    path('', TimetableView.as_view(), name='home'),
    path('update', UpdateTimetableView.as_view(), name='update_timetble'),
    path('test', TimetableApiView.as_view(), name='update_timetable'),
    path('course', CourseListApiView.as_view(), name='course'),
]