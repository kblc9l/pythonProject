import sqlite3


def get_oll_result(id_person):
    try:
        con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT wpm, cpm, accuracy FROM result WHERE people = '{id_person}'""").fetchall()
        con.close()
        wpm, cpm, accuracy = [], [], []
        if result:
            for i in result:
                wpm.append(i[0])
                cpm.append(i[1])
                accuracy.append(i[2])
            return wpm, cpm, accuracy
        else:
            return [0], [0], [0]
    except Exception as er:
        print(er)


def get_id_user():
    with open('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/data/login_data.txt', 'r', encoding='utf8') as f:
        login, password = [i.rstrip() for i in f.readlines()]
    try:
        con = sqlite3.connect('C:/Users/Professional/PycharmProjects/pythonProject/blidingtype/database.sqlite')
        cur = con.cursor()
        result = cur.execute(
            f"""SELECT id FROM people WHERE login = '{login}' and password = '{password}'""").fetchall()
        con.close()
        print(result)
        return result[0][0]
    except Exception as er:
        print(er)
