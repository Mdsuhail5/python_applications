import requests
import datetime as dt
import smtplib
import time

# Your position (Bangalore, India coordinates)
MY_LAT = 12.971599
MY_LONG = 77.594566

# Your email credentials
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_specific_password"


def is_iss_overhead():
    """Check if ISS is close to my current position"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is within +/- 5 degrees of my position
    return (MY_LAT-5 <= iss_latitude <= MY_LAT+5 and
            MY_LONG-5 <= iss_longitude <= MY_LONG+5)


def is_night():
    """Check if it's dark enough to see the ISS"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour
    return time_now >= sunset or time_now <= sunrise


def send_email():
    """Send notification email"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky!"
        )


# Run the checking code every 60 seconds
while True:
    # If ISS is close to my current position and it's dark
    if is_iss_overhead() and is_night():
        send_email()

    # Print current status for debugging
    print(f"ISS Overhead: {is_iss_overhead()}")
    print(f"Is Night: {is_night()}")
    print("Checking again in 60 seconds...")

    time.sleep(60)
