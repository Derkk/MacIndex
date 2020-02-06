from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

incognito_mode = webdriver.ChromeOptions()
incognito_mode.add_argument("--incognito")

# call my Chrome driver to start my webpage analysis
chromeDriver = webdriver.Chrome(executable_path='/Users/florianhenrion/Documents/Programming/MacSoftware/ChromeDriver/chromedriver')

# looking for the macbook 13" shopping page

chromeDriver.get("https://www.apple.com/be-fr/shop/buy-mac/macbook-pro/13-pouces")

# get price of the current macbook-pro-13-in BE by using the class name

Current_price = chromeDriver.find_elements_by_class_name("as-price-currentprice") # if you look at the first price class

# try to print the value of this class which should be the price of the product

for priceScan in Current_price:
    print(priceScan.get_attribute("class"))

# waiting the page to load
time.sleep(15)

# close the browser after scan

chromeDriver.quit()





