from database import db

def save_user_in_database(username, password):
    con = db()
    cursor = con.cursor()
    cursor.execute("insert into users (username, password) values(?, ?)", (username, password,))
    con.commit()
    con.close()

def get_user_detail(username):
    con = db()
    cursor = con.cursor()
    cursor.execute("select id, password from users where username = ?", (username,))
    user_detail = cursor.fetchone()
    return user_detail

def get_username_by_user_id(user_id):
    con = db()
    cursor = con.cursor()
    cursor.execute("select username from users where id = ?", (user_id,))
    username = cursor.fetchone()[0]
    return username

