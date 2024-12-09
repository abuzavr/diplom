'''Представления (Views) для задач
Функционал:

task_list: список задач пользователя, с фильтрацией по статусу и поиском.
task_detail: детальный просмотр задачи.
task_create: создание новой задачи.
task_update: редактирование задачи.
task_delete: удаление задачи.
Отдельный экшен для отметки задачи как выполненной task_toggle_complete (опционально).'''

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))

    category_slug = request.GET.get('category')
    if category_slug:
        tasks = tasks.filter(category__slug=category_slug)

    tag_slug = request.GET.get('tag')
    if tag_slug:
        tasks = tasks.filter(tags__slug=tag_slug)

    status = request.GET.get('status')
    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            form.save_m2m()
            messages.success(request, "Задача создана.")
            return redirect('tasks:task_detail', pk=task.pk)
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Создать задачу'})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Задача обновлена.")
            return redirect('tasks:task_detail', pk=task.pk)
    else:
        form = TaskForm(user=request.user, instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Редактировать задачу'})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.info(request, "Задача удалена.")
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    messages.success(request, f"Задача {'выполнена' if task.completed else 'отмечена как невыполненная'}.")
    return redirect('tasks:task_detail', pk=task.pk)
