'''В этом файле мы реализуем dashboard_view, которое отобразит статистику пользователя: количество заметок, задач, выполненных задач, последние заметки и ближайшие задачи по дедлайну.'''
'''Примечание:
Здесь предполагается, что в моделях notes.models.Note и tasks.models.Task поля created_at и due_date уже определены, а также что у пользователя есть связанные заметки и задачи по релейшенам user.notes и user.tasks (это обеспечивается внешними ключами в моделях Note и Task).'''

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from notes.models import Note
from tasks.models import Task

@login_required
def dashboard_view(request):
    user = request.user

    # Подсчёт заметок
    note_count = user.notes.count()

    # Подсчёт задач
    task_count = user.tasks.count()
    completed_task_count = user.tasks.filter(completed=True).count()

    # Ближайшие задачи по дедлайну (например, первые 5)
    upcoming_tasks = user.tasks.filter(
        completed=False,
        due_date__isnull=False,
        due_date__gte=now()
    ).order_by('due_date')[:5]

    # Последние 5 заметок (по дате создания)
    recent_notes = user.notes.order_by('-created_at')[:5]

    context = {
        'note_count': note_count,
        'task_count': task_count,
        'completed_task_count': completed_task_count,
        'upcoming_tasks': upcoming_tasks,
        'recent_notes': recent_notes
    }

    return render(request, 'core/dashboard.html', context)
