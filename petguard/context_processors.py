def admin_status(request):
    """
    Adiciona 'is_admin' ao contexto de todos os templates,
    indicando se o usuário faz parte do grupo 'Administradores'.
    """
    is_admin = False
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='Administradores').exists()
    return {"is_admin": is_admin}
