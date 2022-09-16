from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

data_sheet = data_manager.get_flight_data()

if data_sheet[0]["iataCode"] == "":
    city_names = [row["city"] for row in data_sheet]
    print(city_names)
    codes = flight_search.get_destination_code(city_names)
    data_manager.data_update()

