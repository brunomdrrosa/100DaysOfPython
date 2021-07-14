from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import traceback
import sys

data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "GRU"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes(codes)
    sheet_data = data_manager.get_destination_data()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

try:
    price = flight.price
except AttributeError as err:
    exc_traceback = sys.exc_info()[2]
    print(f"No flights found.\n{err}\n{traceback.print_tb(exc_traceback)}")
else:
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Alerta de preço baixo! Apenas R${flight.price} para viajar de {flight.origin_city}-{flight.origin_airport} para {flight.destination_city}-{flight.destination_airport}, do dia {flight.out_date} até {flight.return_date}."
        )