# users/urls.py
from django.urls import path
from . import views

app_name = 'timetable'
urlpatterns = [
    path('', views.TimetableView.as_view(), name='home'),
    path('update', views.UpdateTimetableView.as_view(), name='update_timetble'),
]