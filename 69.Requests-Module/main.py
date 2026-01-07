import requests

# Google ka page mangwaya
response = requests.get("https://www.google.com")

# Check status (200 means Success)
print(response.status_code) 

# Print the HTML content of the page
print(response.text)