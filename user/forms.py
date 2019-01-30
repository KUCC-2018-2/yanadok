from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'nickname', 'email', 'university')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'nickname', 'email')
