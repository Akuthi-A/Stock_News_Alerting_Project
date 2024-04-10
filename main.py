import requests
from twilio.rest import Client

# these are acquired from my free twilio account
account_sid = "ACea0b1e9a06791b257831903522b3e6b8"
auth_token = "9f78c1978a074cdd8b53921db7e44182"

# For STOCK_NAME any stock name can be passed as defined by the stock market
# for this program I will demo this program using the TSLA stock(Tesla stock)
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Below are the API endpoints, API keys, and parameters that will allow us to start working with api
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "3ece353fa14e40dda11b5db5a893f993"
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "language": "en"
}

STOCK_API_KEY = "278AI9O0DUFZOTJH"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# Get yesterday's closing stock price. Start by getting data from stock api
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']

closing_prices = [value["4. close"] for (key, value) in stock_data.items()]


yesterday_close = float(closing_prices[0])
# Get the day before yesterday's closing stock price
day_before_close = float(closing_prices[1])

# Get the positive difference between 1 and 2.
difference_in_close = abs(day_before_close - yesterday_close)
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round((difference_in_close / yesterday_close) * 100)
print(percentage_difference)
indicator = "🔺"
if (yesterday_close - day_before_close) < 0:
    indicator = "🔻"
# Send three news article(get data from news api) related to the stock if there's a large fluctuation(5%)
# in the stock price (percentage_difference > 5)
if percentage_difference > 1:
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()["articles"][:3]
    news_article = [(news["title"], news["description"]) for news in news_data]

    # Send each article as a separate message via Twilio.
    for news in news_article:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {indicator}{percentage_difference}%\n"
                 f"Headline: {news[0]}\n"
                 f"Brief: {news[1]}",
            from_='+12513179180',
            to='+27724664743'
        )
        print(message.status)


