import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
load_dotenv()



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city='Paris', iata_code="PAR"):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }
        TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        #print(f"Your token is {response.json()['access_token']}")
        #print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']


    def get_iata_code(self, city_name):
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        body = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS"
        }
        #print(f"token{self._token}")
        header = {
            "Authorization": f"Bearer {self._token}"
        }

        response = requests.get(url=endpoint, headers=header, params=body)

        #print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time=None):
        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        if to_time != None:
            return_time = to_time.strftime("%Y-%m-%d")
        else:
            return_time = None
        body = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": return_time,
            "adults": 1,
            "nonStop": "true",
            "max": "10",
        }
        # print(f"token{self._token}")
        header = {
            "Authorization": f"Bearer {self._token}"
        }

        response = requests.get(url=endpoint, headers=header, params=body)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("Response body:", response.text)
            return None

        return response.json()