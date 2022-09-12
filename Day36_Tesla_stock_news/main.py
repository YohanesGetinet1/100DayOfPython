import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "5AASHBM03A4EPAGY"
API_ENDPOINT = "https://www.alphavantage.co"
API_ENDPOINT_WITH_PARAM = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey" \
                          "=5AASHBM03A4EPAGY "
NEWS_API = "98a63386c5b443b6865904b52ac90834"
NEWS_URL = "https://newsapi.org/v2/everything"
TWILIO_SID = "AC135319f048e10565dac88dd9757fc68d"
TWILIO_API = "72fdd7732489c337a69a690574cf613c"
PHONE = "+13513005435"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
    "datatype": "json",

}
response = requests.get(url=API_ENDPOINT_WITH_PARAM)
stock_data = response.json()["Time Series (Daily)"]
# print(stock_data)
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]

yesterday_closing = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing = day_before_yesterday["4. close"]
print(yesterday_closing)
print(day_before_yesterday_closing)

difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
diff_per_100 = (difference / float(yesterday_closing)) * 100
print(diff_per_100)
if diff_per_100 > 3:
    parameter = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news = requests.get(NEWS_URL, params=parameter)
    news_data = news.json()["articles"]
    articles = news_data[:3]
    print(articles)

    formatted_news = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]
    client = Client(TWILIO_SID, TWILIO_API)
    for article in formatted_news:
        message = client.messages.create(
            body=article,
            from_="+13513005435",
            to="+13513005435",
        )
