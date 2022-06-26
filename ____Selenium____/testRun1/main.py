from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


# chrome_options = Options()
# chrome_options.add_argument("--headless")

website_1 = 'https://www.geekbuying.com/'
website_2 = 'http://automationpractice.com/index.php'

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get(website_1)


delay = 3  # seconds
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, '(//span[@class="close_btn line_close close_sub"])[1]')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
    pass


close_btn = driver.find_element(
    By.XPATH, '(//span[@class="close_btn line_close close_sub"])[1]')
close_btn.click()

cookies = driver.find_element(By.XPATH, "//span[@class='cookies-close']")
cookies.click()


search = driver.find_element(
    By.XPATH, '//div[@class="search_input"]/input[@id="searchText"]')
search.send_keys("hello")
search.clear()
search.send_keys("laptop" + Keys.ENTER)


search_enter = driver.find_element(
    By.XPATH, '//div[@class="search_input"]/span[@class="search_btn"]')
search_enter.click()


# time.sleep(3)
# language = driver.find_element(By.LINK_TEXT, "Language")
# hover = ActionChains(driver).move_to_element(language)
# hover.perform()

driver.back()

time.sleep(200)
driver.close()
