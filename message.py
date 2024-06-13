import sqlite3

def log_message(conversation_id, sender, message_text):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Messages (conversation_id, sender, message_text) VALUES (?, ?, ?)",
                   (conversation_id, sender, message_text))
    conn.commit()
    conn.close()
