from selenium import webdriver
import time
#from selenium.webdriver.common.by import By

# starting the driver
driver = webdriver.Chrome() #no path as present in /bin
driver.get("https://www.apple.com/be-fr/shop/buy-mac/macbook-pro/13-pouces")

# try to find the element with the full xpath (tried with the short - didn't work too)

headlines = driver.find_elements_by_xpath('/html/body/div[2]/div[7]/div[2]/bundle-selection/div[2]/h1')

for headlineScan in headlines:
   print(headlineScan.get_attribute('h1'))

# currently returning the result "none"

time.sleep(10)
driver.quit()
