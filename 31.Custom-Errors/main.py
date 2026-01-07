user_input = input("Enter number between 5 and 9 (or type 'Quite' to exit):")
if user_input.lower() == "quite":
    print(f"You type {user_input}.So you are quite ")
else:
    try:
        num = int(user_input)
        if num > 9 or num < 5:
            raise ValueError("Value should be between 5 and 9")
        else:
            print(f"You entered {num}")
    except Exception as e:
        print("Error:",e)