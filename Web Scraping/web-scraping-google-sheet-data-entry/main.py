import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

GOOGLE_FORM = "https://forms.gle/zwf5DTXxqhPciewH6"
WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(WEBSITE_URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

flats_list = soup.select("ul li a address")
flats_urls = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
flats_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

flats = [flat.getText().strip().replace("|", "") for flat in flats_list]
urls = [flat['href'] for flat in flats_urls]
prices = [flat.getText().split("/")[0].split("+")[0] for flat in flats_prices]
# print(flats)
# print(urls)
# print(prices)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Set the browser window not to open
chrome_options.add_argument('headless')

for x in range(len(flats_list)):
    time.sleep(1)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(GOOGLE_FORM)
    time.sleep(1)
    address_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_form.send_keys(flats[x])
    price_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form.send_keys(prices[x])
    url_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_form.send_keys(urls[x])
    confirm = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    confirm.click()

    driver.quit()
