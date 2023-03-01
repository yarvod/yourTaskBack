from django.urls import path

from tasks.views import TaskViewSet

urlpatterns = [
    path(
        '',
        TaskViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='list-create'
    ),
    path(
        '<str:pk>/',
        TaskViewSet.as_view(
            {
                'put': 'partial_update',
                'delete': 'destroy',
             },
        ),
        name='update-delete'
    ),
]
