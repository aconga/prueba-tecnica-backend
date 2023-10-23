from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAdminOrReadOnly(permissions.BasePermission):
    message = "Only administrators have permission to perform this action."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.administrator:
            return True

        raise PermissionDenied(detail=self.message)
