import uuid

from ckeditor.fields import RichTextField
from django.db import models

from projects.constants import UserProjectRoles


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(verbose_name='Название', max_length=255)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class UserProjectRelation(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    project = models.ForeignKey(to='Project', on_delete=models.CASCADE, verbose_name='Проект')
    role = models.CharField(choices=UserProjectRoles.CHOICES, verbose_name='Роль пользователя',
                            default=UserProjectRoles.ADMIN, max_length=10)

    class Meta:
        verbose_name = 'Отношение пользователя к проекту'
        verbose_name_plural = 'Отношения пользователей к проектам'
