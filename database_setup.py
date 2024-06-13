import sqlite3

def setup_database():
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Conversations (
        conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ended_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Messages (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id INTEGER,
        sender TEXT CHECK(sender IN ('user', 'chatbot')),
        message_text TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conversation_id) REFERENCES Conversations(conversation_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Responses (
        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT NOT NULL UNIQUE,
        response_text TEXT NOT NULL
    )
    ''')

    predefined_responses = [
        ('hello', 'Hi there! How can I help you today?'),
        ('hi', 'Hello! What can I do for you?'),
        ('bye', 'Goodbye! Have a great day!'),
        ('help', 'I am here to assist you. You can ask me anything!'),
        ('code', 'What about code do you need help?')
    ]

    cursor.executemany('''
    INSERT OR IGNORE INTO Responses (keyword, response_text) VALUES (?, ?)
    ''', predefined_responses)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
