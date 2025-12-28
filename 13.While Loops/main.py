user_input = ""

while user_input != "quit":
    user_input = input("Enter a message (type 'quit' to stop): ")
    
    if user_input != "quit":
        print(f"You said: {user_input}")

print("Goodbye!")