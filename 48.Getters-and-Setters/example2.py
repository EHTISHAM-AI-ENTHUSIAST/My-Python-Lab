class SmartDoor:
    def __init__(self, opening_percent):
        self._opening = opening_percent  # '_' means it's internal/private

    # GETTER: This lets us read the value like a variable
    @property
    def door_status(self):
        return f"The door is {self._opening}% open."

    # SETTER: This checks the value before changing it
    @door_status.setter
    def door_status(self, new_value):
        if new_value < 0 or new_value > 100:
            print("Error: Invalid opening percentage! Must be between 0-100.")
        else:
            self._opening = new_value

# --- Using the class ---
my_door = SmartDoor(50)

# Calling the Getter (No brackets needed!)
print(my_door.door_status) 

# Using the Setter to change value
my_door.door_status = 80
print(my_door.door_status)

# Trying to set an invalid value
my_door.door_status = 500  # This will trigger the Error in Setter