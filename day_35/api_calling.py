import requests
from api import api_key
LAT = 12.971599
LONG = 77.594566

params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
}

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
response = requests.get(
    url=OWM_Endpoint, params=params)

print(response.json())
