import requests
from pprint import pprint
SHETTY_URL = "https://api.sheety.co/fbd5970f6a39f87665740f16cd5ef295/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_flight_data(self):

        shetty_response = requests.get(url=SHETTY_URL)
        flight_data = shetty_response.json()
        # new_dict = {key: value for (key, value) in flight_data.items()}
        self.destination_data = flight_data["prices"]
        return self.destination_data

    def data_update(self):
        for destination in self.destination_data:
            update = {
                "price": {
                    "iataCode": destination["iataCode"]
                }
            }
            post = requests.post(url=f"{SHETTY_URL}/{destination['id']}", json=update)

            print(post.text)
