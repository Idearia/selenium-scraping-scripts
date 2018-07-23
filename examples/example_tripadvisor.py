## Print to screen the reviews from the given TripAdvisor
## restaurant page, in the following format:
## Review's date - Reviewer's name => Rating value

# System dependencies
import os, sys, inspect
import time
import re

# Load Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Load our Selenium library
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+'/includes')
import common

# Webpage to crawl
url = "https://www.tripadvisor.it/Restaurant_Review-g187791-d2321183-Reviews-Sacco_Bistrot-Rome_Lazio.html"

# Main review element, containing all other elements (title, description, ratings...)
review_container_selector = ".review"

# Elements to extract for each review (CSS selectors)
title_selector = ".quote a span"
text_selector = "p.partial_entry"
reviewer_name_selector = ".scrname"
is_mobile_selector = ".viaMobile"
rating_selector = ".review div.rating span.ui_bubble_rating"
date_selector = ".ratingDate"
more_selector = ".ulBlueLinks"

# Navigation element for next page
buttonNext_selector = ".next"

# Select driver (Chrome)
options = webdriver.ChromeOptions()
#options.add_argument('headless')   # Uncomment to use headless browser
driver = webdriver.Chrome(chrome_options=options)

# Get HTML from URL
driver.get(url)

# Wait 6 seconds
time.sleep(6)

# Expand review area
driver.find_element_by_css_selector(more_selector).click()

# Wait 2 seconds
time.sleep(2)

# Get all review containers
review_container_elements = driver.find_elements_by_css_selector(review_container_selector)

# Loop - For each review container, extract its relevant elements
for review in review_container_elements:

    # Get relevant review elements using CSS selectors
    title = common.find_element_text_or_default( review, title_selector)
    date = common.find_element_attribute_or_default( review, date_selector, 'title')
    # reviewer_id = review.find_element_by_class_name('memberOverlayLink').get_attribute('id')
    reviewer_name = common.find_element_text_or_default( review, reviewer_name_selector)
    text = common.find_element_text_or_default( review, text_selector)
    mobile = common.find_element_text_or_default(review, is_mobile_selector)
    rating =  common.find_element_attribute_or_default(review, rating_selector, 'class' )
    rating_value = str(re.findall('[0-9][0-9]', rating)) #ui_bubble_rating bubble_30

    # Print reviews to screen
    common.print_review(title, date, reviewer_name, text, mobile, rating_value)


# Uncomment to go to next page of reviews
#time.sleep(2)
#driver.find_element_by_css_selector(buttonNext).click()

# Close driver
driver.close()