'''Для категорий может быть полезен простейший список или детальная страница. Но пока оставим всё минимальным. Можно добавить URL-ы и вьюхи, если потребуется:'''

from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    # Возможно в будущем: path('', views.category_list, name='category_list'),
    # path('<slug:slug>/', views.category_detail, name='category_detail'),
]
