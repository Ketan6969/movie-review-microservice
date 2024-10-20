# import requests

# # API URL
# url = 'http://127.0.0.1:5000/getall'

# # Send a GET request
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Convert the response to JSON format
#     data = response.json()
#     print("Data retrieved from API:")
#     print(data)
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

import requests

# API URL
url = 'http://127.0.0.1:5000/add_entry'

# Data to be sent in the request body
data = {
    'username': 'example_user',
    'password': 'example_password'
}

# Send a POST request
response = requests.post(url, json=data)

# Print the response
print(response.json())
