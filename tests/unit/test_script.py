# import webdriver
import pytest
from selenium import webdriver
import time
import logging

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(filename='selenium.log', level=logging.INFO)

# Define ChromeOptions to run headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Use ChromeDriverManager to download and manage ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# get url
# only works if we are using live server on our local machine in vs code
driver.get("https://git-action-testing-files.vercel.app/")
index = 1

def test_BrowseRoleListings():
    # ensure that 'staff' is clicked
    staff = driver.find_element(By.ID, "staff")
    staff.click()
    time.sleep(1)

    # check if create button exist
    try:
        driver.find_element(By.XPATH, "//button[@class='btn btn-dark']")
        print("Test case failed. Create button should not exist.")
    except NoSuchElementException:
        # This block will be executed if the element is not found
        print("Create button does not exist.")


    listings = "listing_list"
    try:
        # Find the parent div element with id="listing_list"
        parent_div = driver.find_element_by_id("listing_list")

        # Find all child elements representing individual listings
        listing_elements = parent_div.find_elements_by_css_selector(".card.mb-4")

        # Get the number of listings
        number_of_listings = len(listing_elements)

        # Now you can work with the number of listings as needed
        print("Number of Listings:", number_of_listings)
        # Capture a screenshot and save it
        screenshot_path = f'screenshot_{index}.png'
        driver.save_screenshot(screenshot_path)
        index +=1 
        print("Listings found.")
    except NoSuchElementException:
        print("No listings found.")

    print("End of Test Case")

def ReadRoleListings(): 
    hr = driver.find_element(By.ID, "hr")
    hr.click()
    time.sleep(1)

    # Capture a screenshot and save it
    screenshot_path = f'screenshot_{index}.png'
    driver.save_screenshot(screenshot_path)
    index +=1

#     # find create new role listing button
#     element = driver.find_element(By.XPATH, "//button[@class='btn btn-dark']")
#     actual_create_name = element.text
#     expected_create_name = "Create a Job Listing"

#     # search for job listings 
#     listings = "listing_list"
#     try:
#         element = driver.find_element("id", listings)
#         print("Listings found.")
#         listingLoaded = True
#     except NoSuchElementException:
#         print("No listings found.")
#         listingLoaded = False

#     # search for edit button
#     edit = driver.find_element(By.XPATH, "//button[@class='btn btn-link']")
#     actual_edit_name = edit.text
#     expected_edit_name = "Edit"

#     # check conditions
#     if (actual_create_name == expected_create_name) and listingLoaded and (actual_edit_name == expected_edit_name):
#         print("Test case passed!")
#     else:
#         print("Test case failed.")

# test_BrowseRoleListings()
# ReadRoleListings()
# print("All test cases passed successfully!")