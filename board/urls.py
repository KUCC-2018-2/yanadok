from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.boardView.as_view(), name=''),
    path('<int:course_id>/', views.boardView.as_view(), name='board'),
    url(r'^new_post/$', views.new_post, name='new_post'),
]