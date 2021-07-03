import requests
import smtplib

my_email = "lioalekc@gmail.com"
password = "6E&Z(+OQeg#Y41qs"
MY_LAT = 56.20515
MY_LONG = 69.13896
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a6f84081ce3352200d48f29651d63b22"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data.get("hourly")[:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data.get("weather")[0].get("id")
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg="Subject: Today is rain.\n\n Bring an umbrella.")
