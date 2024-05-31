# Sample FAQ Database (replace with actual data)
faq_data = {
    "application_process": {
        "question": "How do I apply?",
        "answer": "The application process can be found on our website at ggsipu.in"
    },
    "deadlines": {
        "question": "What are the application deadlines?",
        "answer": "The application deadline for Fall semester is typically    20-06-2024. You can find all deadlines on our website at ggsipu.in"
    },
    # Add more FAQ entries for other topics...
}

# Function to store user mentioned topics in a conversation
user_context = []

# Function to greet the user and explain chatbot purpose
def greet_user():
  print("Hi there! I'm your friendly college admission assistant. I can answer your questions about applying to our program. What can I help you with today?")

# Function to handle user questions
def handle_question(question):
  # Identify keywords in the question
  keywords = question.lower().split()

  # Search for matching FAQ entries
  for topic, entry in faq_data.items():
    if any(keyword in question for keyword in keywords):
      # Found a match, return the answer
      user_context.append(topic)  # Update user_context with the matched topic
      return entry["answer"]

  # No match found, handle error
  return "I apologize, I couldn't understand your question. Can you rephrase it?"

# Function to handle multiple questions with basic context awareness and menu
def conversation_loop():
  greet_user()
  while True:
    question = input("You: ")
    if question.lower() == "quit":
      break

    answer = handle_question(question)
    print("Chatbot: " + answer)

    # Leverage user_context for semi-personalized responses
    if len(user_context) > 0:
      # Example: If user asked about deadlines earlier, suggest resources
      if "deadlines" in user_context:
        print("Would you like to see some helpful resources on meeting application deadlines?")

    # Offer menu for frequently asked topics
    print("\nYou can also ask me about:")
    for topic in faq_data.keys():
      print(f"- {topic}")
    print("Is there anything else I can help you with today?")

    user_context.clear()  # Clear user_context after each question

# Start the conversation loop
conversation_loop()
