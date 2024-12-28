import datetime as dt
import random
import smtplib

my_email = "adjeimanuspendilove812@gmail.com"
password = "pyiwybrdnkkiybes"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythondeveloper12@yahoo.com",
                            msg=f"Subject:Monday Motivation!\n\n{random_quote}")
