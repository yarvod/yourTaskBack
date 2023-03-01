import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.timezone import now


class TimeRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE, verbose_name='Задача', related_name='time_records')
    time = models.PositiveIntegerField(verbose_name='Время, секунды')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Запись времени'
        verbose_name_plural = 'Записи времени'


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    parent = models.ForeignKey(
        'Task',
        on_delete=models.SET_NULL,
        verbose_name='Родительская задача',
        related_name='child_tasks',
        blank=True,
        null=True,
    )
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, verbose_name='Проект')
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Создатель', related_name='created_tasks')
    executor = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Исполнитель', related_name='running_tasks')
    title = models.CharField(verbose_name='Название', max_length=255)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    achieved = models.BooleanField(verbose_name='Выполнена', default=False)
    date_deadline = models.DateField(verbose_name='Дата срока выполнения', default=now)
    date_achieved = models.DateField(verbose_name='Дата выполнения', blank=True, null=True)
    time_estimate = models.FloatField(verbose_name='Предположительное время выполнения, часы', blank=True, null=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE, verbose_name='Задача', related_name='comments')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задачам'
