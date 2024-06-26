import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}
        self.sheet_headers = {
            "Content-Type": "application/json",
            "Authorization": os.environ["SHEET_TOKEN"],
        }
        self.destination_data = {}



    def get_data_from_google_sheet(self):
        get_endpoint = "https://api.sheety.co/e80c0d1bd2d5a0a7f8cf548d7ec79c8e/flightDeals/prices"
        response = requests.get(url=get_endpoint, headers=self.sheet_headers)
        data = response.json()
        #pprint(data)
        self.destination_data = data['prices']
        return self.destination_data

    def put_code(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_endpoint = 'https://api.sheety.co/e80c0d1bd2d5a0a7f8cf548d7ec79c8e/flightDeals/prices/'
            response = requests.put(url=f"{put_endpoint}{city['id']}", json=new_data,  headers=self.sheet_headers)
            #print(response.text)