from work_with_db import registration


class LetterError(Exception):
    pass


class LenError(Exception):
    pass


def check_login(login):  # проверка правильности написания логина
    if len(login) < 3:
        raise LenError
    for i in login.lower():
        if i not in 'qwertyuiopasdfghjklzxcvbnm._-1234567890':
            raise LetterError()
    registration.check_login_in_db(login)  # проверка наличие в бд

