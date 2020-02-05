from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

#incognito_mode = webdriver.ChromeOptions()
#incognito_mode.add_argument(“ — incognito”)

chromeDriver = webdriver.Chrome(executable_path='/Users/florianhenrion/Documents/Programming/MacSoftware/ChromeDriver/chromedriver')
#chromeDriver.implicitly_wait(10) # seconds
chromeDriver.get("https://www.apple.com/be-fr/shop/buy-iphone/iphone-11")

# Element that I am currently looking for - price of the current iphone-11

#Current_price = chromeDriver.find_element_by_class_name('price-point price-point-fullPrice')

heading1 = chromeDriver.find_element_by_tag_name('h1')

print('h1')




