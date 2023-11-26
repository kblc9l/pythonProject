import sqlite3


class EmailInDb(Exception):
    pass


class LoginInDb(Exception):
    pass


def entry_to_db(login: str, email: str, password):  # запись данных пользователя в базу данных
    try:
        con = sqlite3.connect('work_with_db/database.sqlite')
        cur = con.cursor()
        request = ("INSERT INTO people (login, email, password) "
                   "VALUES") + f" (\'{login}\', \'{email}\', \'{password}\')"
        cur.execute(request)
        con.commit()
        con.close()
    except Exception as er:
        print(er)


def check_email_in_db(email):  # функция проверки повтора email в базе данных
    con = sqlite3.connect('work_with_db/database.sqlite')
    cur = con.cursor()
    request = f"""SELECT * FROM people WHERE email = '{email}' """
    result = cur.execute(request).fetchall()
    con.close()
    if len(result) != 0:
        raise EmailInDb('Email in db')


def check_login_in_db(login):  # проверка наличие логина в базе данных
    con = sqlite3.connect('work_with_db/database.sqlite')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM people WHERE login = '{login}'""").fetchall()
    con.close()
    if len(result) != 0:
        raise LoginInDb('Login in Db')
