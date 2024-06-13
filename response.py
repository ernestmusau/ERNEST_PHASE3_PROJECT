import sqlite3

def get_response(user_input):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT response_text FROM Responses WHERE keyword = ?", (user_input,))
    response = cursor.fetchone()
    conn.close()
    if response:
        return response[0]
    else:
        return "Sorry, I don't understand that."
