import sqlite3

# Creates the database

def create_table():
    conn = sqlite3.connect('loginfo.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE loginfos (
        user_name text,
        password text,
        phone text
    )''')
    conn.commit()
    conn.close()

def delete_table():
    conn = sqlite3.connect('loginfo.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE loginfos")
    conn.commit()
    conn.close()

create_table()
