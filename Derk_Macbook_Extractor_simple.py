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


price = soup.find('span', {'class':'as-price-currentprice'}).find('span')

print(price)

# You had a 15 second wait here for the page to load. The page loads earlier in the code and Selenium waites for the page to load. When executing things on a page it usually is good to have a 1 sec wait, e.g. clicking a button.
driver.close()
