#To run and test the code you need to update 3 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]
URL = "https://www.amazon.com/BTECH-GMRS-PRO-Waterproof-Bluetooth-Programmable/dp/B0B4BLZ67Z/ref=sr_1_2?content-id=amzn1.sym.3e23f907-b859-4094-8b45-cf96f8c9286b%3Aamzn1.sym.3e23f907-b859-4094-8b45-cf96f8c9286b&dib=eyJ2IjoiMSJ9.MnmXae2s5cgwRkZEzsl1CFdi-acZgKu2Vrz-dOdA4bgQNM4qXkP5PdNJ7HfQY4BPidfgsU1jdcsgIF0rs1_XXCRje6715pHx8P-LnpGMwQJAmyfq8nJjAzqDdUf5fdb4tA6_ROVItFUDEkXAgFgM2piKZRXWPZvgMryFW53cDqc.Ko5ecQOqXhWLFMaTgOH3MdDResrjYAF2igdaQtsT_us&dib_tag=se&keywords=btech+gmrs-v2&pd_rd_r=e151657b-37a8-4e69-afc9-6cd698c25084&pd_rd_w=SMvw2&pd_rd_wg=dhJ6j&pf_rd_p=3e23f907-b859-4094-8b45-cf96f8c9286b&pf_rd_r=6JK0HN48Q7Z15857TSQB&qid=1718605744&sr=8-2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "Accept-Language": "pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
}

response = requests.get(URL, headers=headers)
website_html = response.text
# print(website_html)
soup = BeautifulSoup(website_html, "lxml")
#soup.select("li ul li h3")
# soup.find_all
price_whole = soup.find(class_="a-price-whole")
price_fraction = soup.find(class_="a-price-fraction")
price = float(f'{price_whole.getText()}{price_fraction.getText()}')
price_symbol = soup.find(class_="a-price-symbol")
# print(price)
product = soup.select_one("h1")
# print(product.getText())


if price < 160:
    # Gmail: smtp.gmail.com | port 587
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{product.getText()}\n"
                f"\nprice: {price_symbol.getText()}{price}"
                f"\n \n{URL}")

