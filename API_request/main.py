import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "yuihara23@gmail.com"
MY_PASS = "your APP password"
MY_LONG = 120.252674
MY_LAT = 22.936934

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LONG-5 <= longitude <= MY_LONG+5 and MY_LAT-5 <= latitude <= MY_LAT+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset =  int(data["results"]["sunset"].split('T')[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now()


    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\n The ISS is above you in the sky"
        )
        connection.quit()