print("Chatbot (type 'bye' to exit)")

while True:
    msg = input("You: ").strip().lower()

    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Bot: Hi!")
    elif msg == "how are you":
        print("Bot: I'm fine, thank you! How can I assist you today?")
    elif msg == "what is python":
        print("Bot: Python is a programming language used for web development, data analysis, artificial intelligence, and more.")
    elif msg == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that yet. Please try asking something simple or type 'bye' to exit.")