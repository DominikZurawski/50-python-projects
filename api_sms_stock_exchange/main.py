import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_ALPHA = os.environ.get("API_ALPHA")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_NEWS = os.environ.get("API_NEWS")

TWILLO_NUMBER = os.environ.get("TWILLO_NUMBER")
RECEIVER_NUMBER = os.environ.get("RECEIVER_NUMBER")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


def close_price_2_days():
    parameters = {
        'function': "TIME_SERIES_DAILY",
        'symbol': STOCK_NAME,
        "apikey": API_ALPHA,
        "outputsize": "compact",
    }

    response = requests.get(url=STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    print(response.json())
    data = response.json()['Time Series (Daily)']
    new_data = {k: data[k] for k in list(data)[:2]}
    close_prices = (new_data[list(new_data)[0]]['4. close'], new_data[list(new_data)[1]]['4. close'])
    print(close_prices)
    diff = float(close_prices[0]) - float(close_prices[1])
    #abs_diff = abs(diff)
    print(diff)
    percentage_diff = (diff / float(close_prices[0])) * 100
    return percentage_diff


def news():
    parameters = {
        'q': COMPANY_NAME,
        #"from": datetime.now().date(),
        "sortBy": "popularity",
        "apikey": API_NEWS,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    #print(response.json())
    data = response.json()

    articles = [f"Headline: {msg['title']}. \nBrief:{msg['description']}" for msg in data['articles'][:3]]
    for article in articles:
        send_sms(article)


def send_sms(msg):
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_=TWILLO_NUMBER,
        to=RECEIVER_NUMBER
    )

    print(message.status)


if close_price_2_days() > 3:
    news()
