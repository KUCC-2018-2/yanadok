from django.contrib import admin
from .models import Post, PostLike, Comment

admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)