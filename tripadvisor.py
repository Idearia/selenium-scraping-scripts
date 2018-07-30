## Print to screen the reviews from the given TripAdvisor
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
import review_functions

# Webpage to crawl
url = sys.argv[1] #https://www.tripadvisor.it/Restaurant_Review-g187791-d2321183-Reviews-Sacco_Bistrot-Rome_Lazio.html

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
page_name_selector = ".heading_title"
page_number_selector = "a.pageNum.last.taLnk"

# Navigation element for next page
buttonNext_selector = "a.next.ui_button"
review_number = 0
page_number = 1
page_number_tot = int

# Select driver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument('headless')   # Uncomment to use headless browser
driver = webdriver.Chrome(chrome_options=options)

# Each 'find' by Selenium has this amount of time to work
driver.implicitly_wait(1)

# Get HTML from URL
driver.get(url)
common.wait_for_page_load()
page_number_tot = common.find_element_text_or_default(driver, page_number_selector)

# Get Title for CSV
page_name = driver.find_element_by_css_selector(page_name_selector).text

# Add CSV heading
review_functions.trip_setting_csv(page_name)

# Initialize counters
page_number = 0
review_number = 0

# Loop through review pages; the condition is that the navigation button
# can be clicked.
while True: # each iteration is a review page

    # Track page number
    page_number += 1
    review_number_in_current_page = 0

    print( '>>>>>>>>>>>> PAGE NUMBER %d <<<<<<<<<<<<<<<<<<' % page_number )

    # Get all review containers
    review_container_elements = driver.find_elements_by_css_selector(review_container_selector)

    # Expand review area by clicking on the "Click for more" button
    try:
        click_for_more_element = driver.find_element_by_css_selector(more_selector)
        if click_for_more_element.is_enabled():
            click_for_more_element.click()
    # Ok if the button does not exist: it means all reviews on the
    # page are short
    except:
        pass

    # Loop through the list of review containers and for each them scrape the
    # relevant review elements
    for review in review_container_elements:

        # Increment counters
        review_number += 1
        review_number_in_current_page += 1

        print( '_______ Review number %d ________' % review_number_in_current_page )

        # Initialize review dictionary
        review_dict = {}
        
        # Get relevant review elements using CSS selectors
        review_dict['title'] = common.find_element_text_or_default(review, title_selector)
        review_dict['date'] = common.find_element_attribute_or_default(review, date_selector, 'title')
        review_dict['reviewer_name'] = common.find_element_text_or_default(review, reviewer_name_selector)
        review_dict['text'] = common.find_element_text_or_default(review, text_selector)
        review_dict['mobile'] = common.find_element_text_or_default(review, is_mobile_selector)
        review_dict['rating'] =  common.find_element_attribute_or_default(review, rating_selector, 'class')
        # review_dict['reviewer_id'] = review.find_element_by_class_name('memberOverlayLink').get_attribute('id')

        # Sanitize review elements
        if len(review_dict['rating']) > 2:
            review_dict['rating'] = review_dict['rating'][-2:-1] #ui_bubble_rating bubble_30

        # Validate review dictionary
        # review_functions.validate_review(review_dict)

        # # Uncomment to print reviews to screen
        review_functions.trip_print_review(review_dict)

        # # Uncomment to export results in csv file
        review_functions.trip_export_review(review_dict, page_name)

    # Determine whether we are on the last page
    last_page = False
    next_button_element = driver.find_element_by_css_selector(buttonNext_selector)
    try:
        last_page = common.element_is_disabled(next_button_element)
    except:
        last_page = True

    # If we are not on the last page, try to advance to the next page.
    # Otherwise, stop trying and break the loop.
    if last_page:
        break
    else:
        next_button_element.click()
        common.wait_for_page_load()
        print( '\n' )


driver.close()