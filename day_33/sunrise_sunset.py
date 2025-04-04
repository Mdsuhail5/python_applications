import requests
import datetime as dt

MY_LAT = 12.971599  # Bangalore latitude
MY_LONG = 77.594566  # Bangalore longitude


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(
        url="https://api.sunrise-sunset.org/json",
        params=parameters
    )
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now()
    current_hour = time_now.hour

    # Check if it's dark (before sunrise or after sunset)
    return current_hour <= sunrise or current_hour >= sunset


def get_formatted_times():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(
        url="https://api.sunrise-sunset.org/json",
        params=parameters
    )
    response.raise_for_status()
    data = response.json()

    sunrise_time = data["results"]["sunrise"].split("T")[1].split(":")
    sunset_time = data["results"]["sunset"].split("T")[1].split(":")

    return {
        "sunrise": f"{sunrise_time[0]}:{sunrise_time[1]}",
        "sunset": f"{sunset_time[0]}:{sunset_time[1]}"
    }


if __name__ == "__main__":
    times = get_formatted_times()
    print(f"Sunrise: {times['sunrise']}")
    print(f"Sunset: {times['sunset']}")

    if is_dark():
        print("It's dark outside!")
    else:
        print("It's light outside!")

    time_now = dt.datetime.now()
    print(f"Current time: {time_now.hour}:{time_now.minute}")
