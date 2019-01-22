from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'university', 'email', 'first_name', 'last_name', 'nickname')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'university', 'email', 'first_name', 'last_name', 'nickname')
