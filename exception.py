class BaseServerError(Exception):
    code = 500
    message = 'Непредвиденная ошибка'


class ItemNotFound(BaseServerError):
    code = 404
    message = 'Не найдено'


class UserAlreadyExists(BaseServerError):
    code = 400
    message = 'Пользователь уже существует'
