def user_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

user_details(name="Ahmed", city="Lahore")
print("---")
user_details(name="Sana", age=25, occupation="Doctor")