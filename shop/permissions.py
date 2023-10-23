from rest_framework import permissions


class IsProductCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the authenticated user is the creator of the product
        return obj.user == request.user
