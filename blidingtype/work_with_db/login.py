import sqlite3


class NotLoginInDb(Exception):
    pass


class IncorrectPassword(Exception):
    pass


def check_login_in_db(login):  # проверка наличие логина в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE login = '{login}'""").fetchall()
    con.close()
    if len(result) == 0:
        raise NotLoginInDb('Login not in db')


class NotPasswordInDb(Exception):
    pass


def check_cor_password_in_db(login, password):  # проверка наличия пароля в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT login FROM people WHERE password = '{password}'""").fetchall()
    con.close()
    if result:
        if result[0][0] != login:
            raise IncorrectPassword('incorrect password')
    else:
        raise IncorrectPassword('incorrect password')