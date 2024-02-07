from rest_framework.permissions import BasePermission


class IsModeratorOrOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        elif view.get_object().owner == request.user:
            return True
        else:
            return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.get_object().owner == request.user:
            return True
        else:
            return False

