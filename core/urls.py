from django.urls import path
from .views import dashboard_view  # Импортируем вьюху

# Указываем пространство имён для маршрутов приложения core
app_name = 'core'

# Определяем маршруты
urlpatterns = [
    # Маршрут для Dashboard
    path('', dashboard_view, name='dashboard'),  # Главная страница
]
