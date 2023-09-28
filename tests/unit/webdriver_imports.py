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
driver.get("http://127.0.0.1:5500/frontend/index.html")