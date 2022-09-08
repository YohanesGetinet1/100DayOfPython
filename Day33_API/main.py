import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351
MY_LONG = -0.127758
My_EMAIL = "skillpickethiopia@gmail.com"
MY_PASSWORD = "*********"


def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_near() and is_night_time():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(My_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL,
                            msg="Subject:Check the sky the iss is over your head\n\n"
                                "")
