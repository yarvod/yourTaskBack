from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from authentication.authenticate import CustomAuthentication
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    authentication_classes = (CustomAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = (
            Task.objects.all()
            .prefetch_related('comments')
            .select_related('executor', 'creator')
        )
        if self.action in ('list', 'retrieve', 'update'):
            return queryset.filter(
                Q(creator=self.request.user) |
                Q(executor=self.request.user)
            )
        return queryset

    def get_serializer_class(self):
        return TaskSerializer

