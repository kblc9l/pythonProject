class LetterError(Exception):
    pass


class LenError(Exception):
    pass


def check_login(login):
    if len(login) < 3:
        raise LenError
    for i in login.lower():
        if i not in 'qwertyuiopasdfghjklzxcvbnm._-1234567890':
            raise LetterError()

    # проверка наличие в бд
