from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission



def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


class IsAdminOrReadOnly(IsAuthenticated):

    def has_permission(self, request, view):

        # First, check authentication
        if not super().has_permission(request, view):
            return False

        # Allow authenticated users to read
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        # Only staff users can perform write operations
        return request.user.is_staff

class RoleAndOwnerPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # The user must be logged in.
        if not user or not user.is_authenticated:
            return False

        # All three roles can view student records.
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        # ADMIN can perform all operations.
        if in_group(user, "ADMIN"):
            return True

        # TRAINER can create and update, but not delete.
        if in_group(user, "TRAINER"):
            return request.method in ("POST", "PUT", "PATCH")

        # STUDENT is read-only.
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        # All roles can view individual records.
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        # ADMIN can modify any record.
        if in_group(user, "ADMIN"):
            return True

        # TRAINER can modify only records they created.
        if in_group(user, "TRAINER"):
            return obj.created_by_id == user.id

        return False
