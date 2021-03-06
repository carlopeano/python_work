def send_messages(messages, sent_messages):
    """
    Print every message
    Move each message to a new list called sent_messages
    """
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

text_messages = [
    "Hey, how are you?",
    "I miss you my Dear",
    "Life is beautiful",
    "It's raining today",
    "I've bought the present for Mary",
    ]
sent_messages = []

send_messages(text_messages[:], sent_messages)

print()
for text_message in text_messages:
    print(text_message)