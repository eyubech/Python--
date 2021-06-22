import sqlite3
db = sqlite3.connect("app.db")


cr = db.cursor()

cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")


cr.execute(f"insert into users(user_id, name) values('1', 'data')")
cr.execute(f"insert into users(user_id, name) values('2', 'rome')")
cr.execute(f"insert into users(user_id, name) values('3', 'python')")

cr.execute("select user_id, name from users")

print(cr.fetchall())




db.commit()
db.close()