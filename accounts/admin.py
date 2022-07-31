from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['mobile_number', 'full_name', 'class_name']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number', 'full_name', 'class_name', 'subject_name')}),
    )

    ordering = ['full_name']


admin.site.register(MyUser, MyUserAdmin)
