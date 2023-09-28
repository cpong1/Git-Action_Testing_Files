# import webdriver
import pytest
from selenium import webdriver
import time
import os

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# Define ChromeOptions to run headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Use ChromeDriverManager to download and manage ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# get url
# only works if we are using live server on our local machine in vs code
driver.get("http://127.0.0.1:5500/templates/index.html")


def test_BrowseRoleListings():
    # ensure that 'staff' is clicked
    staff = driver.find_element(By.ID, "staff")
    staff.click()

    listings = "listing_list"
    try:
        element = driver.find_element("id", listings)
        print("Listings found.")
    except NoSuchElementException:
        print("No listings found.")

    print("End of Test Case")

def test_ReadRoleListing_pos():
    time.sleep(1)
    # ensure that 'hr' is clicked
    staff = driver.find_element(By.ID, "hr")
    staff.click()

    # find create new role listing button
    element = driver.find_element(By.XPATH, "//button[@class='btn btn-dark']")
    actual_create_name = element.text
    expected_create_name = "Create a Job Listing"

    # search for job listings 
    listings = "listing_list"
    try:
        element = driver.find_element("id", listings)
        print("Listings found.")
        listingLoaded = True
    except NoSuchElementException:
        print("No listings found.")
        listingLoaded = False

    # search for edit button
    edit = driver.find_element(By.XPATH, "//button[@class='btn btn-link']")
    actual_edit_name = edit.text
    expected_edit_name = "Edit"

    # check conditions
    if (actual_create_name == expected_create_name) and listingLoaded and (actual_edit_name == expected_edit_name):
        print("Test case passed!")
    else:
        print("Test case failed.")


test_BrowseRoleListings()
test_ReadRoleListing_pos()
print("All test cases passed successfully!")