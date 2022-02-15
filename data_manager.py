from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c49020829a158e84fbc469348ba9441f/flightDeals/prices"
SHEETY_EMAILS_ENDPOINT = "https://api.sheety.co/c49020829a158e84fbc469348ba9441f/flightDeals/users"
headers = {
    "Authorization": f"Bearer {12345667}",
    "Content-Type": "application/json",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_customer_email(self):
        response = requests.get(url=SHEETY_EMAILS_ENDPOINT,headers=headers)
        data = response.json()["users"]
        self.customer_data = data
        return self.customer_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

