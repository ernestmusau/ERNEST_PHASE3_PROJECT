import sqlite3

def get_or_create_user(username):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
    else:
        cursor.execute("INSERT INTO Users (username) VALUES (?)", (username,))
        user_id = cursor.lastrowid
        conn.commit()
    conn.close()
    return user_id
