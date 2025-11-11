from rest_framework import permissions

class IsAdministrador(permissions.BasePermission):
    """
    Permissão que permite acesso apenas aos usuários do grupo 'Administradores'.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name='Administradores').exists()
        )
