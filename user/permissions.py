# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from user.models import User
from mentor.models import Mentor

class IsMember(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(
                email = request.user,
                is_mentor=False,
                is_active=True
                )
        except User.DoesNotExist:
            return False
        return True

class IsActiveMentor(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.select_related('mentor').get(
                email=request.user,
                is_mentor=True,
                is_active=True,
                ).mentor
        except User.DoesNotExist:
            return False
        return True

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(
                email=request.user,
                is_staff=True,
                is_active=True,
                )
        except User.DoesNotExist:
            return False
        return True
