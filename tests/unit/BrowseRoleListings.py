# import webdriver
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# create webdriver object
driver = webdriver.Chrome()
# get url
driver.get("http://127.0.0.1:5500/templates/index.html")

listings = "listing_list"
try:
    element = driver.find_element("id", listings)
    print("Listings found.")
except NoSuchElementException:
    print("No listings found.")

print("End of Test Case")
