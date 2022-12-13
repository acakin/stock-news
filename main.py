import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "***"
NEWS_API = "***"

FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
SYMBOL = "TSLA"

account_sid = "***"
auth_token = "***"


param_stock = {
    "function": FUNCTION,
    "symbol": SYMBOL,
    "apikey": STOCK_API
}
r_stock = requests.get(STOCK_ENDPOINT, params=param_stock)
data_stock = r_stock.json()
yesterday_price = [(data_stock["Time Series (Daily)"][_]["4. close"]) for _ in data_stock["Time Series (Daily)"]]
difference_of_close = float(yesterday_price[0]) - float(yesterday_price[1])
percentage_of_difference = difference_of_close / float(yesterday_price[1]) * 100

if percentage_of_difference > 0:
    icon = "🔺"
else:
    icon = "🔻"

COMPANY_NAME = "Tesla"
DOMAIN = "bloomberg.com,reuters.com,economist.com,wsj.com"
param_news = {
    "q": COMPANY_NAME,
    "domain": DOMAIN,
    "apiKey": NEWS_API,
}

r_news = requests.get(NEWS_ENDPOINT, params=param_news)
data_news = r_news.json()

if abs(percentage_of_difference) > 5:
    client = Client(account_sid, auth_token)
    for _ in range(0,3):
        message = client.messages \
            .create(
            body=f"TSLA: {icon}{round(abs(percentage_of_difference), 6)}"
                 f"Headline: {data_news['articles'][_]['title']} "
                 f"Brief: {data_news['articles'][_]['description']} "
                 f"url: {data_news['articles'][_]['url']}",
            from_='+1***',
            to='+90***'
        )
        print(message.status)


else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"TSLA: {icon}{round(abs(percentage_of_difference), 6)}",
        from_='+1***',
        to='+90***'
    )

    print(message.status)





