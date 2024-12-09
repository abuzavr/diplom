from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags')
