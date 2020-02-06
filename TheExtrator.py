from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

incognito_mode = webdriver.ChromeOptions()
incognito_mode.add_argument("--incognito")

chromeDriver = webdriver.Chrome(executable_path='/Users/florianhenrion/Documents/Programming/MacSoftware/ChromeDriver/chromedriver')

#chromeDriver.implicitly_wait(20) # seconds
chromeDriver.get("https://www.apple.com/be-fr/shop/buy-mac/macbook-pro/13-pouces")

# Element that I am currently looking for - price of the current macbook-pro-13-in BE
Current_price = chromeDriver.find_elements_by_class_name("as-price-currentprice")

for priceScan in Current_price:
    print(priceScan.get_attribute("class"))


time.sleep(15)
chromeDriver.quit()





