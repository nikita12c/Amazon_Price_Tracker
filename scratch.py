import requests
from bs4 import BeautifulSoup
import smtplib
import time

# from requests.exceptions import ConnectionError


URL = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B08445DF23/ref=redir_mobile_desktop?ie=UTF8&aaxitk=JRR-urbfhsIOWwTcUCScIA&hsa_cr_id=9024981630302&ref_=sb_s_sparkle'

headers = {
    "User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def check_price():
    # try:

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    # print(soup.prettify())

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price).get_text()

    if (converted_price > 60000):
        send_mail()
    print(title.strip())
    # print(converted_price.strip())
    print(page.status_code)


# except ConnectionError:
# print("please connect")

check_price()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('chaudharinikita9999@gmail.com', 'sknapetgithlxyjq')

    subject = 'Hey...Nikita Price fell Down !'
    body = 'Check th Amazon Link https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B08445DF23/ref=redir_mobile_desktop?  ie=UTF8&aaxitk=JRR-urbfhsIOWwTcUCScIA&hsa_cr_id=9024981630302&ref_=sb_s_sparkle'

    msg = f"Subject:{subject}\n\n{body}"

    server.send_mail(
        'chaudharinikita9999@gmail.com',
        'nikita.chaudhari121199@gmail.com',
        msg
    )
    print("HEY EMAIL SENT SUCCESFULLY")

    server.quit()

# while(True):
#   check_price()
#   time.sleep(60*60*24)