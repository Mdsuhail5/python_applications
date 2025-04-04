# HTTP.requests()
from datetime import datetime
import requests

# GET request    requests.get()    ask external system for data
# POST request    requests.post()   we give data to external system and are only interesed in it was successful or not
# PUT request    requests.put()     updates a piece of data in external system
# DELETE request    requests.delete()  deletes a piece of data in external system

TOKEN = "asdfgkjkljlerei832jjf"
USERNAME = "raj9090"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# to create a new user using post method
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# posting the data
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()


value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How manykilometers did you cycle today? "),
}

response = requests.post(
    url=value_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# update_params = {
#     "quantity": "4.5"
# }
# # response = requests.put(url=update_endpoint,
# #                         json=update_params, headers=headers)
# # print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
