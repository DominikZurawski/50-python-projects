import requests
from datetime import datetime
from time import sleep
import smtplib

MY_LAT = 51.930489
MY_LONG = 22.379000
# Here put the email address, password, receiver email
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "PASSWORD"

count = 0
latitude = None
longitude = None

def get_ISS_data():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    global latitude, longitude
    latitude = float(response.json()["iss_position"]['latitude'])
    longitude = float(response.json()["iss_position"]['longitude'])


def get_sunset_sunrise():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": 'Europe/Warsaw'
    }
    try:
        response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
    except:
        global count
        count += 1
        print(f'Try: {count}')
        get_sunset_sunrise()
    else:
        sunrise = int(response.json()["results"]["sunrise"].split('T')[1].split(":")[0])
        sunset = int(response.json()["results"]["sunset"].split('T')[1].split(":")[0])
        return (sunrise, sunset)


def my_position_range(x):
    return x - 5, x + 5


def if_in_range(num, t):
    down_num = t[0]
    up_num = t[1]
    return down_num <= num <= up_num


def is_iss_overhead():

    my_lat_range = my_position_range(MY_LAT)
    my_long_range = my_position_range(MY_LONG)
    get_ISS_data()

    if if_in_range(latitude, my_lat_range) and if_in_range(longitude, my_long_range):
        print(latitude, longitude)
        return True
    else:
        print("ISS not is overhead!")


def is_night():
    time_now = datetime.now()

    if not if_in_range(time_now.hour, get_sunset_sunrise()):
        return True


is_night()
is_iss_overhead()

while True:
    sleep(60)
    if is_night() and is_iss_overhead():
        # For Gmail: smtp.gmail.com | Hotmail: smtp.live.com | Yahoo: smtp.mail.yahoo.com
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up👆\n\nThe ISS is above you in the sky.")


