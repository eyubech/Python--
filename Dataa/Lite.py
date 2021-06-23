import sqlite3

db = sqlite3.connect("app.db")
cr = db.cursor()

cr.execute("delete from users where user_id = 3 ")


cr.execute("select * from users")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

