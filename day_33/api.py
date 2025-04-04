# API: application programming interface
# An api is a set of commands,functions, protocols, and objects that programmers can use to create software,or interact with an external system.
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# to check which is the response code
response.raise_for_status()

# response code
# 1XX (Hold on)       something is happening
# 2XX  (Here you go)  Success
# 3XX  (Go Away)    no permission
# 4XX  (You Screwed Up)  doesnt exists
# 5XX   (I Screwed Up)  server is down
data = response.json()
print(data)

latitude = data["iss_position"]["latitude"]
print(latitude)
longitude = data["iss_position"]["longitude"]
print(longitude)

iss_position = (latitude, longitude)
print(iss_position)
