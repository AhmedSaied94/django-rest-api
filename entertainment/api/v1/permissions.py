from rest_framework.permissions import BasePermission

class have_cr_per(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='creaters').exists()
        