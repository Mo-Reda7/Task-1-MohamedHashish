# Rule-Based AI Chatbot

# Knowledge Base (Intent -> Response)
responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "help": "You can greet me or ask simple questions.",
    "bye": "Goodbye!",
    "exit": "Chat ended."
}

print("=== AI Chatbot Started ===")
print("Type 'exit' to quit.\n")

# Infinite Loop
while True:

    # Raw Input
    raw_input_user = input("You: ")

    # Input Sanitization & Normalization
    cleaned_input = raw_input_user.lower().strip()

    # Exit Strategy
    if cleaned_input == "exit":
        print("Bot:", responses.get("exit"))
        break

    # Response Generation
    reply = responses.get(
        cleaned_input,
        "I do not understand."
    )

    print("Bot:", reply)

print("\n=== Chatbot Stopped ===")