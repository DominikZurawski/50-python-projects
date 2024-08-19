from selenium import webdriver
from selenium.webdriver.common.by import By
import time


URL = "https://orteil.dashnet.org/experiments/cookie/"

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

clicker = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

def check_addition():
    list_prices = driver.find_elements(By.CSS_SELECTOR, value="div b")
    prices = [int(el.text.split("-")[1].strip().replace(',', '')) for el in list_prices[-9:-1]]
    #print(prices)
    prices_reverse = prices[::-1]

    # Create dictionary of store items and prices
    cookie_upgrades = {}
    for n in range(len(prices)):
        cookie_upgrades[prices[n]] = item_ids[n]

    current_money = int(money.text.replace(',', ''))

    # Find upgrades that we can currently afford
    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if cost:
            if current_money > cost:
                affordable_upgrades[cost] = id

    # Purchase the most expensive affordable upgrade
    highest_price_affordable_upgrade = max(affordable_upgrades)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

    driver.find_element(by=By.ID, value=to_purchase_id).click()

timeout = time.time() + 5  # 5 sec from now
five_min = time.time() + 60*5  # 5 minutes

while True:
    clicker.click()
    if time.time() > timeout:
        check_addition()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

# # To close one card:
# driver.close()
# # To close browser:
# .quit()
