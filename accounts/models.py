# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

def avatar_upload_path(instance, filename):
    """
    Определяет путь загрузки аватара:
    media/avatars/user_<id>/<filename>
    """
    return f"avatars/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    """
    Профиль пользователя расширяет стандартную модель User,
    добавляя поле аватара и при необходимости дополнительные данные.
    """

    # Связь один-к-одному с встроенной моделью пользователя Django
    # related_name='profile' позволяет обращаться к профилю через user.profile
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="Пользователь"
    )

    # Поле для хранения аватара пользователя, можно загрузить изображение
    # null=True, blank=True означают, что поле не обязательное
    avatar = models.ImageField(
        "Аватар",
        upload_to=avatar_upload_path,
        null=True,
        blank=True,
    )

    # Дополнительные поля, если необходимо:
    # bio = models.TextField("О себе", blank=True, null=True)
    # website = models.URLField("Личный сайт", blank=True, null=True)
    # location = models.CharField("Город", max_length=100, blank=True, null=True)

    # Добавим метаданные модели
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        """
        Возвращает строковое представление профиля.
        Обычно это имя пользователя.
        """
        return f"Profile of {self.user.username}"

    @property
    def avatar_url(self):
        """
        Возвращает URL аватара, если он есть, иначе возвращает URL дефолтной картинки.
        Допустим, у нас есть 'static/img/default_avatar.png' как дефолтный аватар.
        """
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/img/default_avatar.png'

    def delete_old_avatar(self):
        """
        При необходимости можно реализовать удаление старого аватара при загрузке нового.
        Вызывайте этот метод вручную перед сохранением нового аватара, если нужно.
        """
        if self.avatar:
            if os.path.isfile(self.avatar.path):
                os.remove(self.avatar.path)

# Сигнал, который автоматически создаёт профиль при создании нового пользователя.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Когда создаётся новый User, создаём и связанный Profile.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    При сохранении User, сохраняем связанный Profile.
    """
    instance.profile.save()
