import sqlite3
with sqlite3.connect('xkcd_db.db') as con:
    cur = con.cursor()
    cur.execute('drop table if exists xkcd')
    cur.execute('create table xkcd (url text, alt text)')
    cur.execute("insert into xkcd values ('some title', 'fake url')")
    con.commit()