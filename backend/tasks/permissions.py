from rest_framework.permissions import BasePermission


class IsTaskCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.creator == request.user)


class IsTaskExecutor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.executor == request.user)
