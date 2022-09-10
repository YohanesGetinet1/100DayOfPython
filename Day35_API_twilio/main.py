import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


account_sid = os.environ['AC135319f048e10565dac88dd9757fc68d']
auth_token = os.environ['b77d7e8348d7308ea50206fc5487ab38']

api_key = "0a90f9af2d0da06d15e748d75520aca8"
api_url = "https://api.openweathermap.org/data/2.5/onecall"

# lat = 51.507351
# long = -0.127758
parameter = {
    "lat": 51.507351,
    "lon": -0.127758,
    # "q": "London",
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url=api_url, params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to take an umbrella  ",
        from_='+13513005435',
        to='+15558675310'
    )
    print(message.status)
