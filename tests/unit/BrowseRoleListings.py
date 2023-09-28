from webdriver_imports import *

listings = "listing_list"
try:
    element = driver.find_element("id", listings)
    print("Listings found.")
except NoSuchElementException:
    print("No listings found.")

print("End of Test Case")
