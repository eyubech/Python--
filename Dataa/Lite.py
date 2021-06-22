import sqlite3
db = sqlite3.connect("app.db")


cr = db.cursor()

cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")


cr.execute("insert into users(user_id, name) values(1, 'ayoub')")
cr.execute("insert into users(user_id, name) values(2, 'ahmed')")
cr.execute("insert into users(user_id, name) values(3, 'youssef')")



db.commit()
db.close()