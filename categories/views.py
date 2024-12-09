from django.shortcuts import render, get_object_or_404
from .models import Category

# При необходимости можем реализовать функции просмотра категорий.
# Например:
# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'categories/category_list.html', {'categories': categories})

# def category_detail(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     # Можно отфильтровать заметки по категории, когда у нас будут заметки
#     return render(request, 'categories/category_detail.html', {'category': category})
