from django.shortcuts import render, get_list_or_404
from taggit.models import Tag
from notes.models import Note

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})

def tag_detail(request, slug):
    # Получаем тег по slug
    tag = get_list_or_404(Tag, slug=slug)
    # Фильтруем заметки, у которых есть этот тег
    notes = Note.objects.filter(tags__slug=slug, user=request.user)
    return render(request, 'tags/tag_detail.html', {'tag': tag[0], 'notes': notes})
