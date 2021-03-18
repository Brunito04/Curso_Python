import smtplib
import datetime as dt
import random


MY_EMAIL = "brunitotest@gmail.com"
PASSWORD = "Huqz3snrybwVL3"

# --------------------- DATE TIME ------------------------------#
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Tuesday Motivation\n\n{quote}")