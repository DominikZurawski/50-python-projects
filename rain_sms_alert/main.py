import requests
from twilio.rest import Client
import os

MY_LAT = 51.930489
MY_LONG = 22.379000
# You should generate your API on: https://api.openweathermap.org
API = os.environ.get("OWM_API_KEY")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

TWILLO_NUMBER = os.environ.get("TWILLO_NUMBER")
RECEIVER_NUMBER = os.environ.get("RECEIVER_NUMBER")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    "cnt": 4,
    'appid': API,
}


def forecast():
    response = requests.get(url=ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    will_rain = False
    will_rain = forecast_rain(data['list'])
    if will_rain:
        send_sms()

def forecast_rain(list):
    for element in list:
        if element["weather"][0]["id"] < 700:
            return True

def send_sms():
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_=TWILLO_NUMBER,
        to=RECEIVER_NUMBER
    )

    print(message.status)



if __name__ == '__main__':
    forecast()


