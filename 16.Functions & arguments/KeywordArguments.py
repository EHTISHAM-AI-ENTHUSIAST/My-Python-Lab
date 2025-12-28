def student_info(name, subject, marks):
    print(f"Name: {name}, Subject: {subject}, Marks: {marks}")

# Order is important when using positional arguments
student_info("Ali", "Math", 85)

# Order is not important when using keyword arguments
student_info(marks=90, name="Sara", subject="Physics")