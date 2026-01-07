import time

t = time.localtime()
# Formatting: Day-Month-Year Hour:Minute:Second
formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", t)

print(f"Current Date and Time: {formatted_time}")