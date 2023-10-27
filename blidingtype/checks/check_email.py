from email_validate import validate


#  https://docs-python.ru/packages/modul-validate-email-python/  ссылка на этот модуль проверки email

class UnCorrectEmail(Exception):
    pass


def check_email(email):  # функция проверки корректность введённого email
    if not validate(email_address=email, check_format=True, check_blacklist=False, check_dns=False, check_smtp=False,
                    smtp_debug=False):
        raise UnCorrectEmail()

    # ещё будет проверка на наличее в бд
