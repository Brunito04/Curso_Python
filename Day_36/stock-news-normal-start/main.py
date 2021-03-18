import requests
import smtplib
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = '+19256607171'
VERIFIED_NUMBER = '+541131145270'

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_API_KEY = 'BCLGHUXT41C57DJU'
NEWS_API_KEY = '0ca1330a06ad422483fe2e44daeef902'
TWILIO_SID = 'AC6a8da8ea9b4ab655976521c069af9171'
TWILIO_AUTH_TOKEN = '39f0b96936f9fa4cb9382a6b2e925106'

# Get yesterday's closing stock price
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]

    print(formatted_articles)

    # Your email goes here
    my_email = 'brunitotest@gmail.com'
    password = 'Huqz3snrybwVL3'

    # Smtp direction goes here
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # Encrypts the email if intercepted
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='bruno2004b@gmail.com',
            msg=f'Subject:Tesla: {diff_percent}%'
        )
