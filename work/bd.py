import sqlite3

genre = input()
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
result = cur.execute(f"""SELECT DISTINCT Artist.name FROM Artist
    INNER JOIN Album ON Album.ArtistId = Artist.ArtistId
        INNER JOIN Track ON Track.AlbumId = Album.AlbumId
            INNER JOIN Genre ON Track.GenreId = Genre.GenreId
                WHERE Genre.Name = '{genre}'
    ORDER BY Artist.name""").fetchall()
for elem in result:
    print(*elem)
con.close()