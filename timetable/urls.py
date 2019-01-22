# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetableView.as_view(), name='home'),
    path('update', views.updateTimetableView.as_view(), name='update_timetble'),
]