import datetime as dt
import random
import smtplib
import pandas

my_email = "example@mail.com"
password = "password"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient="records")

for friend in birthday_list:
    if today == (friend.get("month"), friend.get("day")):
        name = friend.get("name")
        email = friend.get("email")
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            letter_contents = letter_file.read()
            new_letter = letter_contents.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"Subject:Happy Birthday!\n\n {new_letter}")
