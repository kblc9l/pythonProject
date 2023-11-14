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
    con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE login = '{login}'""").fetchall()
    con.close()
    if len(result) == 0:
        raise NotLoginInDb('Login not in db')


def check_cor_password_in_db_login(login, password):  # проверка наличия пароля в базе данных
    con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT login FROM people WHERE password = '{password}'""").fetchall()
    con.close()
    if result:
        for i in result:
            if login in i:
                break
        else:
            raise IncorrectPassword('incorrect password')
    else:
        raise IncorrectPassword('incorrect password')


def check_cor_password_in_db_email(email, password):  # проверка наличия пароля в базе данных
    con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT email FROM people WHERE password = '{password}'""").fetchall()
    con.close()
    if result:
        for i in result:
            if email in i:
                break
        else:
            raise IncorrectPassword('incorrect password')
    else:
        raise IncorrectPassword('incorrect password')


def check_email_in_db(email):
    con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE email = '{email}'""").fetchall()
    con.close()
    if len(result) == 0:
        raise NotEmailInDb('Login not in db')


def change_password(login, new_password):
    con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
    cur = con.cursor()
    if login.count('@') == 0:
        cur.execute(f"""UPDATE people SET password = '{new_password}' WHERE login = '{login}'""")
    else:
        cur.execute(f"""UPDATE people SET password = '{new_password}' WHERE email = '{login}'""")
    con.commit()
    cur.close()
