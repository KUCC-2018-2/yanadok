from django import forms

from .models import Post, Comment, PostLike


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_type', 'title', 'content', ]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', ]


class PostLikeForm(forms.ModelForm):

    class Meta:
        model = PostLike
        fields = []



