letter_combinations = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю', 'жэё',
                       '1234567890']  # словосочетания букв


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class SpaceError(Exception):
    pass


def check_password(password):  # проверка написания пароля
    if ' ' in password:
        raise SpaceError('SpaceError')
    if not (len(password) > 8):
        raise LengthError('LengthError')
    if not (password.lower() != password and password.upper() != password):
        raise LetterError('LetterError')
    if not (set('0123456789') & set(password)):
        raise DigitError('DigitError')
    for i in range(len(password) - 2):
        if password[i:i + 3].lower() in letter_combinations[0] or password[i:i + 3].lower() in letter_combinations[
            1] or password[i:i + 3].lower() in letter_combinations[2] or password[i:i + 3].lower() in \
                letter_combinations[
                    3] or password[i:i + 3].lower() in letter_combinations[4] or password[i:i + 3].lower() in \
                letter_combinations[
                    5] or password[i:i + 3].lower() in letter_combinations[6] or password[i:i + 3].lower() in \
                letter_combinations[7]:
            raise SequenceError('SequenceError')
    return 'ok'
