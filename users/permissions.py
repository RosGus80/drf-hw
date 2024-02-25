from rest_framework.permissions import BasePermission


class IsUserOrModerator(BasePermission):
    def has_permission(self, request, view):
        if view.get_object() == request.user:
            return True
        elif request.user.groups.filter(name='moderator').exists():
            return True
        else:
            return False


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        else:
            return False