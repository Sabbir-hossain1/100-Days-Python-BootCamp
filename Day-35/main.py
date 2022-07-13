import requests
import os
from twilio.rest import Client

api_key = "0b92a74b84affa7c871c78b5a04e69c0"
api_key1 = "0b92a74b84affa7c871c78b5a04e69c0"
open_weather_map = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "hidden accound sid(use your account_sid)"
auth_token = "hidden authon token(use your auth_token)"

parameters = {
    "lat": 23.797911,
    "lon": 90.414391,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(open_weather_map, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]
will_rain = False
for hourly_data in weather_data:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='This message is from twilo.com',
        from_='+16504054617',
        to='+8801826559551'
    )
    print(message.status)
