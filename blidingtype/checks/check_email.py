import sqlite3

from email_validate import \
    validate  # https://docs-python.ru/packages/modul-validate-email-python/  ссылка на этот модуль проверки email

from blidingtype.work_with_db import registration


class UnCorrectEmail(Exception):
    pass


def check_email(email):  # функция проверки корректность введённого email
    if not validate(email_address=email, check_format=True, check_blacklist=False, check_dns=False, check_smtp=False,
                    smtp_debug=False):
        raise UnCorrectEmail()

    registration.check_email_in_db(email)
