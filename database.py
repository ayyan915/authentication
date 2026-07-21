import sqlite3

def db():
    con = sqlite3.connect("data.db")
    return con

con = db()
cursor = con.cursor()
cursor.execute("""create table if not exists users(
               id integer primary key autoincrement,
               username text unique,
               password text
               )""")