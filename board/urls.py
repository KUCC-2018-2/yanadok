from django.urls import path
from . import views

urlpatterns = [
    path('', views.boardView.as_view(), name='board'),
]