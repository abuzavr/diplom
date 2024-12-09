from django.urls import path
from .views import tag_list, tag_detail

app_name = 'tags'

urlpatterns = [
    path('', tag_list, name='tag_list'),
    path('<slug:slug>/', tag_detail, name='tag_detail'),
]
