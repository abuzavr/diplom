'''Представления (Views) для Notes
Функционал:

note_list: список заметок, с поиском по ключевым словам.
note_detail: детальный просмотр заметки.
note_create: создание новой заметки.
note_update: редактирование заметки.
note_delete: удаление заметки.
Фильтрация по категории и тегам можно делать через GET-параметры или отдельные вьюхи.'''

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note
from .forms import NoteForm
from django.db.models import Q

@login_required
def note_list(request):
    """
    Вывод списка заметок текущего пользователя.
    Поддержка поиска по заголовку и содержимому.
    Можно добавить фильтрацию по категории или тегам через GET параметры.
    Пример: ?q=search_term&category=slug&tag=tag_name
    """
    notes = Note.objects.filter(user=request.user)
    query = request.GET.get('q')
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    category_slug = request.GET.get('category')
    if category_slug:
        notes = notes.filter(category__slug=category_slug)

    tag_slug = request.GET.get('tag')
    if tag_slug:
        notes = notes.filter(tags__slug=tag_slug)

    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def note_detail(request, pk):
    """
    Детальный просмотр заметки.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def note_create(request):
    """
    Создание новой заметки.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()  # Сохраняем теги
            messages.success(request, "Заметка создана.")
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm(user=request.user)

    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Создать заметку'})


@login_required
def note_update(request, pk):
    """
    Редактирование существующей заметки.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Заметка обновлена.")
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note, user=request.user)

    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Редактировать заметку'})


@login_required
def note_delete(request, pk):
    """
    Удаление заметки.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "Заметка удалена.")
        return redirect('notes:note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

