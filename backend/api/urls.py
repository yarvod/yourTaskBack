from django.urls import path, include

urlpatterns = [
    path('common/', include(('common.urls', 'common'))),
    path('auth/', include(('authentication.urls', 'authentication'))),
    path('users/', include(('users.urls', 'users'))),
    path('tasks/', include(('tasks.urls', 'tasks'))),
]
