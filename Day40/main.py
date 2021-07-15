from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "GRU"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Alerta de preço baixo! Apenas R${flight.price} para viajar de {flight.origin_city}-{flight.origin_airport} para {flight.destination_city}-{flight.destination_airport}, do dia {flight.out_date} até {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nO voo tem {flight.stop_overs} escala, na cidade {flight.via_city}."

        link = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        
        notification_manager.send_emails(emails, message, link)