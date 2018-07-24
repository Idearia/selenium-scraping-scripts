## Print to screen the reviews from the given Facebook
## restaurant page, in the following format:
## Review's date - Reviewer's name => Rating value

# System dependencies
import os, sys, inspect
import time
import re
import csv

# Load Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Load our Selenium library
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,currentdir+'/includes')
import common

# Webpage to crawl
url = input("Paste the URL:  ") #https://www.facebook.com/pg/FreddoGelatoRoma/reviews/

# Main review element, containing all other elements (title, description, ratings...)
review_container_selector = "._1dwg"

# buttons
not_now = "expanding_cta_close_button"

# Elements to extract for each review (CSS selectors)
text_selector = "p"
reviewer_name_selector = ".profileLink"
rating_selector = "._51mq"
date_selector = "._5ptz"
page_name_selector = "._64-f span"

# Select driver (Chrome)
options = webdriver.ChromeOptions()
#options.add_argument('headless')   # Uncomment to use headless browser
driver = webdriver.Chrome(chrome_options=options)

# Get HTML from URL and open cookies
driver.get(url)

# Wait 6 seconds
time.sleep(6)

# Scroll Down
timer = time.time() + 15
while time.time() < timer:
    driver.execute_script("window.scrollTo(0,   document.body.scrollHeight);")

if driver.find_element_by_id(not_now).is_enabled():
    driver.find_element_by_id(not_now).click()

# Get all review containers
review_container_elements = driver.find_elements_by_css_selector(review_container_selector)

# Loop - For each review container, extract its relevant elements
for review in review_container_elements:

    # Get relevant review elements using CSS selectors
    date = common.find_element_attribute_or_default( review, date_selector, 'title')
    reviewer_name = common.find_element_text_or_default( review, reviewer_name_selector)
    text = common.find_element_text_or_default( review, text_selector)
    rating =  common.find_element_text_or_default(review, rating_selector)
    rating_value = str(re.findall('[0-9]', rating)) #5 stella to 5

    # Uncomment to print reviews to screen
    common.face_print_review(reviewer_name, date, rating_value, text)

# Close driver
driver.close()