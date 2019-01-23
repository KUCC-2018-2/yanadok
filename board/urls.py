from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.boardView.as_view(), name='board'),
    url(r'^new_post/$', views.new_post, name='new_post'),
]