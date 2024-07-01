from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options =webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

login = driver.find_element(By.NAME, value='fName')
login.send_keys("Domin")
last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys("Domin")
email = driver.find_element(By.NAME, value='email')
email.send_keys("xyz@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

# driver.quit()