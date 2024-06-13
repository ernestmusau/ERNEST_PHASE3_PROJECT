import sqlite3
import datetime

def start_conversation(user_id):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Conversations (user_id) VALUES (?)", (user_id,))
    conversation_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return conversation_id

def end_conversation(conversation_id):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Conversations SET ended_at = ? WHERE conversation_id = ?",
                   (datetime.datetime.now(), conversation_id))
    conn.commit()
    conn.close()
