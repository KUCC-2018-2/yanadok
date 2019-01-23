# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TimetableView.as_view(), name='home'),
    path('update', views.UpdateTimetableView.as_view(), name='update_timetble'),
]