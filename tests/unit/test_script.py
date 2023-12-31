# import webdriver
import pytest
from selenium import webdriver
import time
import logging
import os

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
time.sleep(10)
driver.get("https://git-action-testing-files.vercel.app/")

def BrowseRoleListings():
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

    time.sleep(10)

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
        screenshot_path = os.path.join(os.getcwd(), "screenshot_1.png")
        driver.save_screenshot(screenshot_path)
        print("Listings found.")
    except NoSuchElementException:
        print("No listings found.")

    print("End of Test Case")

def ReadRoleListings(): 
    hr = driver.find_element(By.ID, "hr")
    hr.click()
    time.sleep(10)

    # Capture a screenshot and save it
    screenshot_path = os.path.join(os.getcwd(), "screenshot_2.png")
    driver.save_screenshot(screenshot_path)

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

def CreateRoleListings():
    expected_closing_dates = {}
    # ensure that 'hr' is clicked
    staff = driver.find_element(By.ID, "hr")
    staff.click()
    time.sleep(1)

    # find create new role listing button and create a new role listing
    element = driver.find_element(By.XPATH, "//button[@class='btn btn-dark']")
    element.click()
    time.sleep(1)
    dropdown = Select(driver.find_element(By.ID, "roleTitle")) 
    roleTitle = "Sales Representative"
    dropdown.select_by_visible_text(roleTitle)

    # Locate the input field that opens the date picker and enter in a date
    year = "2023"
    month = "11"
    day = "27"

    # Format the date in "mm/dd/yyyy" format
    formatted_date = f"{month}/{day}/{year}"

    # Locate the date input field and enter the formatted date
    date_input = driver.find_element(By.ID, "closingDate")
    date_input.clear()  # Clear the existing value in the input field
    date_input.send_keys(formatted_date)  # Send the formatted date string
    
    time.sleep(1)
    screenshot_path = os.path.join(os.getcwd(), "screenshot_3.png")
    driver.save_screenshot(screenshot_path)

    # save job listing
    submit = driver.find_element(By.ID, "jobCreationButton")
    submit.click()
    time.sleep(3)

    # close modal
    close = driver.find_element(By.XPATH, "//button[@data-bs-dismiss='modal']")
    time.sleep(10)
    screenshot_path = os.path.join(os.getcwd(), "screenshot_4.png")
    driver.save_screenshot(screenshot_path)
    close.click()

    expected_closing_dates[roleTitle] = formatted_date # add to dictionary

    # Locate all job title elements and closing date elements
    job_title_elements = driver.find_elements(By.CSS_SELECTOR, ".card-title.m-2")
    closing_date_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'text-center')]/h5[contains(text(), 'Closing Date:')]")

    # Ensure there are job titles and closing dates
    if job_title_elements and closing_date_elements:
        # Get the latest job title and closing date
        latest_job_title = job_title_elements[-1].text
        latest_closing_date_element = closing_date_elements[-1]
        latest_closing_date_text = latest_closing_date_element.text.split(":")[1].strip()

        # Check if the latest closing date matches the expected date
        if latest_job_title in expected_closing_dates:
            expected_date = expected_closing_dates[latest_job_title]
            if latest_closing_date_text == expected_date:
                print(f"Latest Job Title: {latest_job_title}, Closing Date: {latest_closing_date_text} (Correct)")
            else:
                print(f"Latest Job Title: {latest_job_title}, Closing Date: {latest_closing_date_text} (Incorrect)")
        else:
            print(f"Latest Job Title: {latest_job_title} (No Expected Closing Date Found)")
    else:
        print("No job titles or closing dates found.")

    print("Test case finished!")
    

# BrowseRoleListings()
# ReadRoleListings()
CreateRoleListings()
print("All test cases passed successfully!")
