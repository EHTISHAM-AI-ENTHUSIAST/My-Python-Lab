command = input("Enter a command like 'hello', 'bye', or 'help': ")

match command:
    case "hello":
        print("Hello there!")
    case "bye":
        print("Goodbye!")
    case "help":
        print("You asked for help.")
    case _:  # This is the default case
        print("Unknown command.")