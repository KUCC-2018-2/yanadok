# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetableView.as_view(), name='timetable'),
    path('update', views.updateTimetableView.as_view(), name='update_timetble'),
]