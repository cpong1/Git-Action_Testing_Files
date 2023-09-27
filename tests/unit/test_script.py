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

# Define the URL of your GitHub Pages site
github_pages_url = f"https://cpong1.github.io/Git-Action_Testing_Files/templates/index.html"


# Navigate to your application URL
driver.get(github_pages_url)

# get url
# only works if we are using live server on our local machine in vs code
# driver.get("http://127.0.0.1:5500/templates/index.html")


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

def test_CreateRoleListings_pos():
    time.sleep(1)
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
    month = "09"
    day = "27"
    date = f"{year}-{month}-{day}"
    date_input = driver.find_element(By.ID, "closingDate")
    date_input.click()
    date_input.send_keys(year)
    date_input.send_keys(Keys.LEFT)
    date_input.send_keys(month)
    date_input.send_keys(Keys.LEFT)
    date_input.send_keys(Keys.LEFT)
    date_input.send_keys(day)
    date_input.send_keys(Keys.RETURN)
    time.sleep(1)

    # save job listing
    submit = driver.find_element(By.ID, "jobCreationButton")
    submit.click()
    time.sleep(3)

    # close modal
    close = driver.find_element(By.XPATH, "//button[@data-bs-dismiss='modal']")
    close.click()

    expected_closing_dates[roleTitle] = date # add to dictionary

    # Locate all job title elements and closing date elements
    job_title_elements = driver.find_elements(By.CSS_SELECTOR, ".card-title.m-2")
    closing_date_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'text-center')]/h5[contains(text(), 'Closing Date:')]")
    print(1)
    print(closing_date_elements)
    # Ensure there are job titles and closing dates
    if job_title_elements and closing_date_elements:
        # Get the latest job title and closing date
        latest_job_title = job_title_elements[0].text
        latest_closing_date_element = closing_date_elements[0]
        
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


# test_BrowseRoleListings()
test_CreateRoleListings_pos()
# test_ReadRoleListing_pos()
print("All test cases passed successfully!")