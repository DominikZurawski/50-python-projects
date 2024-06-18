from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PROMISED_DOWN = 150
PROMISED_UP = 10


TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f'Download: {self.up}')
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f'Upload: {self.down}')

    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")

        time.sleep(2)
        google = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
        google.click()
        time.sleep(2)

        base_window = self.driver.window_handles[0]
        google_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(google_login_window)
        print(self.driver.title)
        # Login and hit enter
        email = self.driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
        email.send_keys(TWITTER_EMAIL)
        send = self.driver.find_element(By.XPATH, value='//*[@id="identifierNext"]')
        send.click()
        time.sleep(4)
        password = self.driver.find_element(By.XPATH, value='//*[@id="pass"]')
        #password.send_keys(FB_PASSWORD)
        password.send_keys(Keys.ENTER)
        # email = self.driver.find_element(By.XPATH,
        #                                  value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        # email.send_keys(TWITTER_EMAIL)
        # time.sleep(3)
        # confirm = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        # confirm.click()
        # time.sleep(1)
        # password = self.driver.find_element(By.XPATH,
        #                                     value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]')
        # password.send_keys(TWITTER_PASSWORD)
        # time.sleep(2)
        # login_btn = self.driver.find_element(By.XPATH,
        #                                    value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        # login_btn.click()
        #
        # time.sleep(5)
        # tweet_compose = self.driver.find_element(By.XPATH,
        #                                          value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        #
        # tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        # tweet_compose.send_keys(tweet)
        # time.sleep(3)

        #tweet_button = self.driver.find_element(By.XPATH,
        #                                        value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        #tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# TODO: connect to twitter
# Still not working authentication by google
# bot.tweet_at_provider()
