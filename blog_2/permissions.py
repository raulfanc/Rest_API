from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """this class is to check if the user is the author of the post"""
    def has_object_permission(self, request, view, obj):
        """this function is to check if the user is the author of the post"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

