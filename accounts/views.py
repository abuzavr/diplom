# Представления (Views)

'''profile_view позже будет дополнен статистикой, когда у нас будут модели заметок и задач.
profile_edit_view обновляет данные о пользователе и его профиль (аватар).
password_change_view позволяет менять пароль без разлогинивания.'''

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm, MyPasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm

def register_view(request):
    """
    Регистрация новых пользователей.
    При успешной регистрации — автоматический логин.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect('notes:note_list')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Вход пользователя. Если пользователь уже залогинен — редирект.
    """
    if request.user.is_authenticated:
        return redirect('notes:note_list')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы успешно вошли!")
            return redirect('notes:note_list')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Выход пользователя из системы.
    """
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect('notes:note_list')


@login_required
def profile_view(request):
    """
    Просмотр профиля пользователя.
    Показать статистику: количество заметок, количество задач,
    выполненные задачи, и т.д. (Позже добавим подсчет)
    """
    user = request.user
    # Можно добавить подсчет заметок и задач, когда будут готовы модели notes и tasks
    # Пример (псевдокод):
    # note_count = user.notes.count()
    # task_count = user.tasks.count()
    # done_tasks = user.tasks.filter(status='done').count()

    return render(request, 'accounts/profile.html', {
        'user': user,
        # 'note_count': note_count,
        # 'task_count': task_count,
        # 'done_tasks': done_tasks,
    })


@login_required
def profile_edit_view(request):
    """
    Редактирование профиля: изменение username, email, аватара.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Профиль обновлён.")
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def password_change_view(request):
    """
    Смена пароля пользователя.
    После смены пароля — обновляем session_auth_hash, чтобы не разлогинило.
    """
    if request.method == 'POST':
        form = MyPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль успешно изменён.")
            return redirect('accounts:profile')
    else:
        form = MyPasswordChangeForm(user=request.user)

    return render(request, 'accounts/password_change.html', {'form': form})
