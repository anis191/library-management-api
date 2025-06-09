from rest_framework import permissions
from users.models import User

class IsLibrarianOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and (request.user.role == User.LIBRARIAN or request.user.is_staff))

class IsLibrarianOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated:
                return True
        
        if request.user.is_staff:
            return True
        
        return request.user.is_authenticated and request.user.role == User.LIBRARIAN