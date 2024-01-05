import random

# Define a list of greetings and responses
greetings = ["hello", "hi", "hey", "greetings", "what's up"]
responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Not much, what about you?"]

# Function to generate a response
def chatbot_response(user_input):
    user_input = user_input.lower()
    for word in greetings:
        if word in user_input:
            return random.choice(responses)
    return "I'm just a simple chatbot. I don't understand that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
