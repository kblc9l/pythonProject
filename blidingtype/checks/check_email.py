import sqlite3

from email_validate import validate


#  https://docs-python.ru/packages/modul-validate-email-python/  ссылка на этот модуль проверки email

class UnCorrectEmail(Exception):
    pass


class EmailInDb(Exception):
    pass


def check_email_in_db(email):  # функция проверки повтора email в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    request = f"""SELECT * FROM people WHERE email = '{email}' """
    print(request)
    result = cur.execute(request).fetchall()
    con.close()
    if len(result) != 0:
        print('email')
        raise EmailInDb('Email in db')


def check_email(email):  # функция проверки корректность введённого email
    if not validate(email_address=email, check_format=True, check_blacklist=False, check_dns=False, check_smtp=False,
                    smtp_debug=False):
        raise UnCorrectEmail()

    check_email_in_db(email)
