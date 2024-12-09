'''Используем datetime-local для ввода даты и времени дедлайна.
Теги подключены аналогично заметкам.'''

from django import forms
from .models import Task
from categories.models import Category
from taggit.forms import TagWidget

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'category', 'tags', 'completed']
        widgets = {
            'tags': TagWidget(),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Отфильтровать категории, если нужно (пока все категории доступны)
        self.fields['category'].queryset = Category.objects.all()
