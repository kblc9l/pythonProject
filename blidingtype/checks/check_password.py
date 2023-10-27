letter_combinations = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю', 'жэё']


class PasswordError(Exception):
    def __init__(self, er):
        super().__init__(er)


class LengthError(PasswordError):
    def __init__(self, er):
        super().__init__(er)


class LetterError(PasswordError):
    def __init__(self, er):
        super().__init__(er)


class DigitError(PasswordError):
    def __init__(self, er):
        super().__init__(er)


class SequenceError(PasswordError):
    def __init__(self, er):
        super().__init__(er)

class SpaceError(Exception):
    pass

def check_password(password):
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
                    5] or password[i:i + 3].lower() in letter_combinations[6]:
            raise SequenceError('SequenceError')
    else:
        return 'ok'
