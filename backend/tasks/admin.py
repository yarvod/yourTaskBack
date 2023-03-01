from django.contrib import admin

from tasks.models import Task, TimeRecord, TaskComment


class TaskCommentInline(admin.StackedInline):
    model = TaskComment
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'achieved', 'creator', 'executor', 'date_deadline', 'time_estimate')
    inlines = (TaskCommentInline,)


@admin.register(TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'task')
