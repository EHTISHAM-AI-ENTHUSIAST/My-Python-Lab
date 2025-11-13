import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)


# Converting hour to integer for comparison
hour = int(time.strftime('%H'))

if 4 <= hour < 12:
    print("Assalam-o-Alaikum, Good morning!")
elif 12 <= hour < 17:
    print("Assalam-o-Alaikum, Good afternoon!")
elif 17 <= hour < 21:
    print("Assalam-o-Alaikum, Good evening!")
else:
    print("Assalam-o-Alaikum, Good night!")
