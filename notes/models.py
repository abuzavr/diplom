'''TaggableManager добавлен для тегов.
category опциональна.
attachment_upload_path определяет, куда загружать файлы.'''

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from taggit.managers import TaggableManager

def attachment_upload_path(instance, filename):
    return f"notes/user_{instance.user.id}/{filename}"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', verbose_name="Пользователь")
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержимое")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    attachment = models.FileField("Вложение", upload_to=attachment_upload_path, blank=True, null=True)
    tags = TaggableManager(verbose_name="Теги", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.title
