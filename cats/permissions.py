from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Сначала в has_permission() проверяется метод запроса и статус пользователя.
    Если метод запроса безопасный (то есть GET, HEAD или OPTIONS) или
    если пользователь аутентифицирован (то есть предоставил валидный токен),
    то метод вернет True. В этом методе доступа к объекту запроса нет,
    поэтому мы не знаем и никак не можем проверить, является ли пользователь,
    делающий запрос, автором объекта.
    Если has_permission() вернул True, то после получения объекта
    вызывается метод has_object_permission(), в него передаётся запрошенный объект,
    и теперь в этом методе можно проверить, совпадает ли автор объекта с пользователем
    из запроса.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):
    """запросы будут разрешены всем"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
