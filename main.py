import re

# Greeting
def greet():
   print("Hello! I'm a chatbot. It's nice to meet you.")

# Basic questions and responses
responses = {
   "hi|hello|hey": "Hello there!",
   "how are you?": "I'm doing well, thanks for asking!",
   "what's your name?": "My name is chater.",
   "what can you do?": "I can answer basic questions, remember our conversation, and ask you some questions too!",
   "goodbye|bye": "Goodbye! It was nice chatting with you."
}

# Previous context
conversation = []

# User interaction
def ask_questions():
   print("Let me ask you a few questions.")
   name = input("What's your name? ")
   conversation.append(("Bot", "What's your name?"))
   conversation.append(("User", name))
   print(f"Nice to meet you, {name}!")

   age = input("How old are you? ")
   conversation.append(("Bot", "How old are you?"))
   conversation.append(("User", age))
   print(f"You're {age} years old.")

   hobby = input("What's your favorite hobby? ")
   conversation.append(("Bot", "What's your favorite hobby?"))
   conversation.append(("User", hobby))
   print(f"That's cool! {hobby} sounds like fun.")

# Error handling
def handle_input(user_input):
   for pattern, response in responses.items():
       if re.search(pattern, user_input, re.IGNORECASE):
           print(response)
           return

   print("I'm sorry, I didn't understand that. Could you rephrase your question?")

# Main loop
def main():
   greet()
   ask_questions()

   while True:
       user_input = input("> ")
       conversation.append(("User", user_input))

       if user_input.lower() == "goodbye" or user_input.lower() == "bye":
           print("Goodbye! It was nice chatting with you.")
           break

       handle_input(user_input)

if __name__ == "__main__":
   main()