from user import get_or_create_user
from conversation import start_conversation, end_conversation
from message import log_message
from response import get_response

def chatbot():
    username = input("Enter your username: ")
    user_id = get_or_create_user(username)
    conversation_id = start_conversation(user_id)
    
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "quit"]:
            log_message(conversation_id, 'user', user_input)
            print("Chatbot: Goodbye!")
            end_conversation(conversation_id)
            break
        log_message(conversation_id, 'user', user_input)
        response = get_response(user_input)
        log_message(conversation_id, 'chatbot', response)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
