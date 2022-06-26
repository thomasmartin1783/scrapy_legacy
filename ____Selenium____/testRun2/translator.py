from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


website_1 = "https://www.google.com/search?ie=UTF-8&q=google%20translator"

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(website_1)

language = driver.find_element(By.XPATH, '//span[@class="source-language"]')
language.click()

time.sleep(2)
bangla = driver.find_element(
    By.XPATH, '//input[@id="sl_list-search-box"]')
bangla.send_keys("bangla" + Keys.ENTER)

input_text = driver.find_element(
    By.XPATH, '//textarea[@id="tw-source-text-ta"]')
input_text.send_keys("ami ghumate jabo")

output_text = driver.find_element(
    By.XPATH, '//div[@id="tw-target-text-container"]//span')
print("*"*50, output_text.text)
time.sleep(.5)
output_text = driver.find_element(
    By.XPATH, '//div[@id="tw-target-text-container"]//span')
print("*"*50, output_text.text)

input_text.clear()
input_text.send_keys("ekhon onek raat")
time.sleep(.5)
print("*"*50, output_text.text)

time.sleep(300)
