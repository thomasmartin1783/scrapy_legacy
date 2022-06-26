from encodings import utf_8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd

xls = pd.ExcelFile(r"Sheet-3.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Column1'].astype('string')

website_1 = "https://translate.google.com/?sl=bn&tl=en"

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(website_1)


input_text = driver.find_element(
    By.XPATH, '//textarea[@aria-label="Source text"]')

out_csv = []

# for i in range(len(var1)):
for i in range(100, 200):
    # print(i)
    try:
        input_text.clear()
        # input_text.send_keys(var1[i])
        driver.execute_script(
            'arguments[0].value=arguments[1]', input_text, var1[i])
        input_text.send_keys(Keys.ENTER)
        # output_text = driver.find_element(
        #     By.XPATH, '//div[@id="tw-target-text-container"]//span')
        # print("*"*50, output_text.text)
        time.sleep(2)
        output_text = driver.find_element(
            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]/span/span')
        output_text_value = output_text.text
        print("*"*50, output_text_value)
        out_csv.append(output_text_value)

        time.sleep(.5)
    except:
        continue

for i in out_csv:
    with open("output_xl3.csv", "ab") as file:
        foo = f"\"{i}\",\n"
        file.write(foo.encode('utf-8'))

time.sleep(100)
driver.close()
