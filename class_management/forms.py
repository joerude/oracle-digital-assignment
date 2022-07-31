from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Student


# class AddStudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"
#
#         widgets = {
#             "full_name": forms.TextInput(attrs={"class": "form-input"}),
#             "email": forms.Textarea(attrs={"cols": 60, "rows": 10}),
#             "birth_date": forms.Textarea(attrs={"cols": 60, "rows": 10}),
#             "class_name": forms.Textarea(attrs={"cols": 60, "rows": 10}),
#             'classroom': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
#             "address": forms.Textarea(attrs={"cols": 60, "rows": 10}),
#             "gender": forms.Textarea(attrs={"cols": 60, "rows": 10}),
#         }


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputUsername",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputPassword",
                "placeholder": "Почта",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputPassword",
                "placeholder": "Пароль",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputPassword",
                "placeholder": "Повторите пароль",
            }
        ),
    )


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputUsername",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputUsername",
                "placeholder": "Пароль",
            }
        ),
    )
