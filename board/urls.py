from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.boardRedirection, name=''),
    path('<int:course_id>/', views.BoardView.as_view(), name='board'),
    path('<int:course_id>/new_post/', views.NewPost.as_view(), name='new_post'),
    path('post/<int:post_id>/edit_post', views.EditPost.as_view(), name='edit_post'),
    path('post/<int:post_id>/delete_post', views.DeletePost.as_view(), name='delete_post'),
    path('post/<int:post_id>', views.PostView.as_view(), name='post'),
    path('post/<int:post_id>/like/', views.PostView.as_view(), name='post_like'),
]

