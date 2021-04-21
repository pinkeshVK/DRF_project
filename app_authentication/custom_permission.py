from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':  # by this you can do only post request can't Get or PUT
            return True
        return False
