from rest_framework.permissions import BasePermission


class UserIsOwnerFundooNotes(BasePermission):

    def has_object_permission(self, request, view, notes):
        return request.user.id == notes.user.id
