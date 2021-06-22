import sqlite3
db = sqlite3.connect("app.db")


cr = db.cursor()

cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")


my_list=['samsung', 'xiaomi', 'iphone', 'lg', 'sony', 'huawei', 'realme']

for key, phone in enumerate(my_list):
    cr.execute(f"insert into users(user_id, name) values({key+1}, '{phone}')")


db.commit()
db.close()