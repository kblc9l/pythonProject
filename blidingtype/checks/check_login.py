import sqlite3


class LetterError(Exception):
    pass


class LenError(Exception):
    pass


class LoginInDb(Exception):
    pass


def check_login_in_db(login):  # проверка наличие логина в базе данных
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE login = '{login}'""").fetchall()
    con.close()
    if len(result) != 0:
        raise LoginInDb('Login in Db')


def check_login(login):  # проверка правильности написания логина
    if len(login) < 3:
        raise LenError
    for i in login.lower():
        if i not in 'qwertyuiopasdfghjklzxcvbnm._-1234567890':
            raise LetterError()
    check_login_in_db(login)
    # проверка наличие в бд
