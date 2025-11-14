# Matching Multiple Values (using |)
# You can use the | (pipe) character to check for several possible values within a single case.



http_status_code = 401

match http_status_code:
    case 200 | 201:
        print("Success! The request was fulfilled.")
    case 401 | 403 | 404:
        print("Client Error! Check your request.")
    case 500 | 503:
        print("Server Error! The server failed.")
    case _:
        print("Some other status code.")