'''Формы для Notes'''

from django import forms
from .models import Note
from categories.models import Category
from taggit.forms import TagWidget

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'tags', 'attachment']
        widgets = {
            'tags': TagWidget(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Если хотим отображать только категории пользователя (если логика такая), 
        # или все категории. Пока допустим все категории.
        self.fields['category'].queryset = Category.objects.all()

