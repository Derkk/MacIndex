# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:51:23 2020

@author: Derk
"""
# BeautifulSoup works well with extracting data from html and xml files, you'd have to install it
from bs4 import BeautifulSoup
from selenium import webdriver

# I use firefox, don't have chrome properly set up for this
driver = webdriver.Firefox()
url = 'https://www.apple.com/be-fr/shop/buy-mac/macbook-pro/13-pouces'

driver.get(url)
# get the html code
html = driver.execute_script('return document.documentElement.outerHTML')
# throw it in beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

# I always take the highest possible level of extraction per product. This way you can also extract other details later on if needed.
Macbooks = soup.find_all('div', {'class':'as-slide-swapper as-macbtr-details'})
print("--------")
for Macbook in Macbooks:
    title = Macbook.find('span', {'class':'label'}).find('span',{'class':'visuallyhidden'}).text
    print(title)
    price_container = str(Macbook.find('span', {'class':'as-price-currentprice'}).find('span'))
    # Very ugly way of cleaning the price. Quite often I have to do it like this since it is the easiest way that works.
    price = price_container.replace(" ","").replace(",",".").replace("€","").replace("<span>","").replace("</span>","")
    print(price)
    print("--------")

# You had a 15 second wait here for the page to load. The page loads earlier in the code and Selenium waites for the page to load. When executing things on a page it usually is good to have a 1 sec wait, e.g. clicking a button.
driver.close()
