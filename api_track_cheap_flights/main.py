#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
import time
from pprint import pprint

data_manager = DataManager()
search = FlightSearch()
data_manager.get_data_from_google_sheet()
sheet_data = data_manager.get_data_from_google_sheet()
# Set your origin airport
ORIGIN_CITY_IATA = "WAW"

for row in sheet_data:
    if sheet_data[0]['iataCode'] == '':
        row['iataCode'] = search.get_iata_code(row["city"])

#print(f"sheet_data:\n {sheet_data}")
data_manager.destination_data = sheet_data
data_manager.put_code()


# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Flights only one way
# for row in sheet_data:
#     lower_price = search.check_flight(
#         origin_city_code=ORIGIN_CITY_IATA,
#         destination_city_code=row["iataCode"],
#         from_time=tomorrow,
#     )
#     print(f"Getting flight for {row['city']}...")
#     try:
#         print(f"{row['city']}: {lower_price['data'][0]['price']['base']} EUR")
#     except IndexError:
#         print(f"{row['city']}: N/A EUR")
#     else:
#         time.sleep(2)


for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = search.check_flight(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: {cheapest_flight.price} EUR")
    # Slowing down requests to avoid rate limit
    time.sleep(2)


