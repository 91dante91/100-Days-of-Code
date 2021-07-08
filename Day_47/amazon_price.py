import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "example@mail.com"
PASWORD = "123456789"
url = "https://www.amazon.com/dp/B001AY0YGU?ref_=Oct_DLandingS_D_8be5e621_NA"
headers = {
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url=url,
                        headers=headers)
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price_span = soup.find(id="priceblock_dealprice")
title_span = soup.find(id="productTitle").getText()
price = float(price_span.getText().split("$")[1])
title = " ".join(title_span.split())


if price < 400:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price alert!\n\n{title} is now {price} \n{url}")
