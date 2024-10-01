import sqlite3



def init_sqlite_db():
    conn=sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE , password TEXT)')
    conn.close()

init_sqlite_db()

def workig(username,password):
    with sqlite3.connect('users.db') as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username,password))
        conn.commit()
        
def loginpage(username,password):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        return cursor.fetchone()
    
def chakuser(username):
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            return cursor.fetchone()
        
