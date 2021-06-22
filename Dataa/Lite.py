import sqlite3
db = sqlite3.connect("app.db")

db.execute("create table skills (name text, progress integer, user_id integer )")