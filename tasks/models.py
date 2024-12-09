'''Модель задач
tasks/models.py'''

'''Порядок сортировки: сначала невыполненные (completed=False), затем по due_date, а выполненные задачи — в конце.
Опционально, можно изменить сортировку.'''

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from taggit.managers import TaggableManager

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name="Пользователь")
    title = models.CharField("Заголовок", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)
    due_date = models.DateTimeField("Дедлайн", blank=True, null=True)
    completed = models.BooleanField("Выполнено", default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    tags = TaggableManager(verbose_name="Теги", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True)

    class Meta:
        ordering = ['completed', 'due_date']
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
