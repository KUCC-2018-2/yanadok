from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardRedirectionView.as_view(), name=''),
    path('<int:course_id>/', views.BoardView.as_view(), name='board'),
    path('<int:course_id>/new_post/', views.NewPost.as_view(), name='new_post'),
]