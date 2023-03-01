from rest_framework import serializers

from tasks.models import Task, TaskComment, TimeRecord


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskComment
        fields = '__all__'


class TimeRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeRecord
        fields = '__all__'
