# Здесь будут формы для регистрации пользователя, входа, обновления профиля и смены пароля.

'''UserRegisterForm использует встроенный UserCreationForm, добавляем проверку уникальности email.
UserLoginForm — простой логин.
UserUpdateForm и ProfileUpdateForm — для обновления данных пользователя и его профиля.
MyPasswordChangeForm — для смены пароля, используем встроенные валидации Django.'''

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import password_validation

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class MyPasswordChangeForm(DjangoPasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput, help_text=password_validation.password_validators_help_texts())
    new_password2 = forms.CharField(label="Подтверждение нового пароля", widget=forms.PasswordInput)

