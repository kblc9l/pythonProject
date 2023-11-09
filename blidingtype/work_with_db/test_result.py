import sqlite3


def write_test_result_in_db(wpm, cpm, accuracy):
    with open('data/login_data.txt', 'r', encoding='utf8') as f:
        login, password = [i.rstrip() for i in f.readlines()]

        id1 = get_id_user(login, password)
    try:
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        request = ("INSERT INTO result (people, wpm, cpm, accuracy) "
                   "VALUES") + f" (\'{id1}\', \'{wpm}\', \'{cpm}\', \'{accuracy}\')"
        print(request)
        cur.execute(request)
        con.commit()
        con.close()
    except Exception as er:
        print(er)


def get_id_user(login, password):
    try:
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT id FROM people WHERE login = '{login}' and password = '{password}'""").fetchall()
        con.close()
        print(result)
        return result[0][0]
    except Exception as er:
        print(er)