import sqlite3

a = []


def kindness(*args, symp_kind):
    con = sqlite3.connect('actions.db')
    cur = con.cursor()
    result = cur.execute(f"""
    SELECT
        People.name, Cities.city, Acts.act
    FROM
        People
    
    LEFT JOIN Acts ON People.city_id = Cities.id
    LEFT JOIN CITIES ON People.act_id = Acts.id
    WHERE
        Acts.kindness_level + Acts.symp_level >= {symp_kind}
    
    """).fetchall()
    con.close()
    for row in result:
        if row[1] in args:
            a.append(row)

    return [i[0] for i in sorted(a, key=lambda x: (len(x[2]), x[0]))]
