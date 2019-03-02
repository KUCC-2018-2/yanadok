from django.urls import path

from timetable.views.api import TimetableApiView, TimetableDeleteApiView
from timetable.views.timetable import TimetableView, UpdateTimetableView

app_name = 'timetable'
urlpatterns = [
    path('', TimetableView.as_view(), name='home'),
    path('update', UpdateTimetableView.as_view(), name='update_timetble'),
    path('timetable', TimetableApiView.as_view(), name='update_timetable'),
    path('timetable/<int:course_id>', TimetableDeleteApiView.as_view(), name='delete_timetable')
]