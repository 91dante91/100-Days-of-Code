import requests
from datetime import datetime, timedelta
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "60HAQKGXRXCV87DO"
my_email = "example@gmail.com"
password = "12345678"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
yesterday = str((datetime.now() - timedelta(1)).date())
day_before = str((datetime.now() - timedelta(2)).date())
price_yesterday = format(float(data["Time Series (Daily)"][yesterday]["4. close"]), '.2f')
price_day_before = format(float(data["Time Series (Daily)"][day_before]["4. close"]), '.2f')
difference = float(price_yesterday) - float(price_day_before)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(price_yesterday)) * 100)

if abs(diff_percent) > -1:
    news_api = "535765b5fae24772955f8950f06ba1e2"

    news_api_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api
    }
    new_response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_parameters)
    new_response.raise_for_status()
    data_news = new_response.json()
    news_pieces = [data_news["articles"][num] for num in range(3)]

    formatted_news = [f"{STOCK}:{up_down}{diff_percent}% \nHeadline: {new['title']}.\nBrief: {new['description']}"
                      for new in news_pieces]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        for new in formatted_news:
            print(new)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:TSLA! \n\n {new}")
