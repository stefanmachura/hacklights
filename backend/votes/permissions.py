from rest_framework import permissions


class IsNotOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author != request.user
