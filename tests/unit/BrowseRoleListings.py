from webdriver_imports import *

# Define the URL of your GitHub Pages site
github_pages_url = f"https://cpong1.github.io/Git-Action_Testing_Files/frontend/index.html?role=staff"

# Navigate to your application URL
driver.get(github_pages_url)

listings = "listing_list"
try:
    element = driver.find_element("id", listings)
    print("Listings found.")
except NoSuchElementException:
    print("No listings found.")

print("End of Test Case")
