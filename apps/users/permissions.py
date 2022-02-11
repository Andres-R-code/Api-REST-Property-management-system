from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):

    def has_permission(self, request, view,):

        if request.method == 'GET' and request.user.is_staff:
            return True


        if request.method == 'POST' and request.user.is_anonymous:
            return True

        return False

    def has_object_permission(self, request,view, obj):

        if request.method == 'DELETE':
            return False

        return True
