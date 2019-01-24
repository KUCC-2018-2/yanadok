from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardRedirectionView.as_view(), name=''),
    path('<int:course_id>/', views.BoardView.as_view(), name='board'),
    path('<int:course_id>/new_post/', views.NewPost.as_view(), name='new_post'),

    # 게시물 페이지가 <int:course_id>/<int:post_id>/ 라고 가정하고 짰어요
    # path('<int:course_id>/<int:post_id>/edit_post', views.EditPost.as_view(), name='new_post'),

    path('post/<int:post_id>', views.PostView.as_view(), name='post'),
    path('post/<int:post_id>/like/', views.PostView.as_view(), name='post_like'),
]