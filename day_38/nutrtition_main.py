import datetime as dt
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables using os.getenv()
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
HOST_DOMAIN = os.getenv("NUTRITIONIX_HOST")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": 'application/json'
}
query = input("Tell me which exercises you did today: ")

params = {
    "query": query,
}
NLP_ENDPOINT = f"{HOST_DOMAIN}/v2/natural/exercise"
response = requests.post(url=NLP_ENDPOINT, json=params, headers=HEADER)
result = response.json()
print(result)
# Exercises = result["exercises"][0]["user_input"]
# Duration = result["exercises"][0]["duration_min"]
# Calories = result["exercises"][0]["nf_calories"]
today = dt.datetime.now()
# print(f"you {Exercises} for {Duration} and burnt {Calories}")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic ZHJlazpkcmVrc2hlZXR5MjQ2OA=="  # Add your bearer token here
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime('%Y-%m-%d'),  # Changed date format
            "time": today.strftime('%H:%M:%S'),
            # Changed to lowercase to match sheet
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]  # Changed to lowercase
        }
    }


response2 = requests.post(
    url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
print(response2.text)
