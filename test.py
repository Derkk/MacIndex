from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.apple.com/be-fr/shop/buy-mac/macbook-pro/13-pouces")

headlines = driver.find_elements_by_xpath('/html/body/div[2]/div[7]/div[2]/bundle-selection/div[2]/h1')

for headline in headlines:
   print(headline.get_attribute('h1'))

time.sleep(10)
driver.quit()
