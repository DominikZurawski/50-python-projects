import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

import time

URL = "https://tinder.com/"
FB_EMAIL = os.environ["FB_EMAIL"]
FB_PASSWORD = os.environ["FB_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# close = driver.find_element(By.CLASS_NAME, value="Z(1) StretchedBox CenterAlign")
# close.click()
# time.sleep(1)
login = driver.find_element(By.XPATH,
                            value='//*[@id="u1584650407"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
login.click()
time.sleep(2)
login1 = driver.find_element(By.XPATH,
                             value='//*[@id="u-143730669"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
login1.click()

#Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

reject_cokie = driver.find_element(By.XPATH,
                             value='//*[@id="u-143730669"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
reject_cokie.click()

time.sleep(5)
location = driver.find_element(By.XPATH, value='//*[@id="u-143730669"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()

notification = driver.find_element(By.XPATH, value='//*[@id="u-143730669"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification.click()
time.sleep(4)
# -- actually hitting like
# driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)
# sleep(4)
# unlike
for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_LEFT)
    time.sleep(1)


