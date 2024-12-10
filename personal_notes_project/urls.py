# Этот файл соединяет все наши приложения в единый маршрутизатор.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Маршруты для аутентификации и аккаунтов
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # Маршруты для заметок
    path('notes/', include('notes.urls', namespace='notes')),

    # Маршруты для задач
    path('tasks/', include('tasks.urls', namespace='tasks')),

    # Подключение маршрутов приложения core
    path('', include('core.urls', namespace='core')),

    # Категории
    path('categories/', include('categories.urls', namespace='categories')),

    # Теги
    path('tags/', include('tags.urls', namespace='tags')),
]

# Добавляем раздачу медиа файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
