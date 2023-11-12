import sqlite3


class NotLoginInDb(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class NotPasswordInDb(Exception):
    pass


class NotEmailInDb(Exception):
    pass


def check_login_in_db(login):  # проверка наличие логина в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE login = '{login}'""").fetchall()
    con.close()
    if len(result) == 0:
        raise NotLoginInDb('Login not in db')


def check_cor_password_in_db_login(login, password):  # проверка наличия пароля в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT login FROM people WHERE password = '{password}'""").fetchall()
    con.close()
    if result:
        if result[0][0] != login:
            raise IncorrectPassword('incorrect password')
    else:
        raise IncorrectPassword('incorrect password')


def check_cor_password_in_db_email(email, password):  # проверка наличия пароля в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT email FROM people WHERE password = '{password}'""").fetchall()
    con.close()
    if result:
        if result[0][0] != email:
            raise IncorrectPassword('incorrect password')
    else:
        raise IncorrectPassword('incorrect password')


def check_email_in_db(email):
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE email = '{email}'""").fetchall()
    con.close()
    if len(result) == 0:
        raise NotEmailInDb('Login not in db')


def change_password(email='', login='', new_password=''):
    pass
