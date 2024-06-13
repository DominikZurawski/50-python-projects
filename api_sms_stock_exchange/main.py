import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_ALPHA = 'M24DFEHHP2CEJZ90'
#API_ALPHA = '9ZID9DTL0JYQ1431'
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_NEWS = "4b44f1d171df4ac7bdaed507188c4474"

ACCOUNT_SID = 'ACc9968fc5d93329e0c14601e79ac74c1b'
AUTH_TOKEN = '021984ed2979d8fc5b07b4a77f802952'
RECEIVER_NUMBER = '+48732187642'
TWILLO_NUMBER = '+17722766916'


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
