from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'first_name', 'last_name', 'nickname',]
    fieldsets = [
        ('Basic Information', {'fields': ['username', 'first_name', 'last_name', 'nickname', 'email', 'university']}),
        ('Authority', {'fields': ['is_superuser', 'is_staff']})

    ]
    list_filter = ['university']


admin.site.register(User, CustomUserAdmin)
