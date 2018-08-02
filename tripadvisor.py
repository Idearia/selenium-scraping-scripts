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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load our Selenium library
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,currentdir+'/includes')
import common
import review_functions

# Webpage to crawl
url = sys.argv[1]
# Sacco Risto:      https://www.tripadvisor.it/Restaurant_Review-g187791-d4355291-Reviews-Ristorante_Sacco-Rome_Lazio.html
# Sacco Bistrot:    https://www.tripadvisor.it/Restaurant_Review-g187791-d2321183-Reviews-Sacco_Bistrot-Rome_Lazio.html
# Freddo:           https://www.tripadvisor.it/Restaurant_Review-g187791-d10455235-Reviews-Freddo-Rome_Lazio.html
# Pepe Gallia:      https://www.tripadvisor.it/Restaurant_Review-g187791-d10800552-Reviews-Pepe-Rome_Lazio.html
# Pepe Tuscolana:   https://www.tripadvisor.it/Restaurant_Review-g187791-d5267113-Reviews-Sacco_Pizza_a_Domicilio-Rome_Lazio.html


# Timeout for element search in seconds
wait_time = 10
wait_page_load = 6
wait_review_load = 2

# Flag for not found element
not_found_flag = "NOT FOUND"

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
reviewer_img_selector = ".avatarImage"

# Navigation element for next page
buttonNext_selector = "a.next.ui_button"
review_number = 0
page_number = 1
page_number_tot = int

# Select driver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument('headless')   # Uncomment to use headless browser
driver = webdriver.Chrome(chrome_options=options)

# Get HTML from URL
driver.get(url)
common.wait_for_(wait_page_load)
page_number_tot = common.find_element_text_or_default(driver, page_number_selector)

# Get Title for CSV
page_name = common.find_element_text_or_default(driver, page_name_selector, not_found_flag, wait_time)

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
    review_container_elements = common.find_elements_or_default(driver, review_container_selector, not_found_flag, wait_time)

    # Expand review area by clicking on the "Click for more" button
    common.click_button(driver, more_selector)

    # Loop through the list of review containers and for each them scrape the
    # relevant review elements
    for review in review_container_elements:

        # Increment counters
        review_number += 1
        review_number_in_current_page += 1

        print('_______ Review number %d ________' % review_number_in_current_page)

        # Initialize review dictionary
        review_dict = {}

        # Give time to Selenium to identify all the selectors and
        # get relevant review elements using CSS selectors
        review_dict['title'] = common.find_element_text_or_default(review, title_selector,not_found_flag,wait_time)
        review_dict['date'] = common.find_element_attribute_or_default(review, date_selector, 'title',not_found_flag,wait_time)
        review_dict['reviewer_name'] = common.find_element_text_or_default(review, reviewer_name_selector,not_found_flag,wait_time)
        review_dict['text'] = common.find_element_text_or_default(review, text_selector,not_found_flag,wait_time)
        review_dict['mobile'] = common.find_element_text_or_default(review, is_mobile_selector,not_found_flag,wait_time)
        review_dict['rating'] =  common.find_element_attribute_or_default(review, rating_selector, 'class',not_found_flag,wait_time)
        # review_dict['reviewer_id'] = review.find_element_by_class_name('memberOverlayLink').get_attribute('id')
        
        # Wait for loading reviews
        common.wait_for_(wait_review_load)
        
        # Sanitize review elements
        if len(review_dict['rating']) > 2:
            review_dict['rating'] = review_dict['rating'][-2:-1] #ui_bubble_rating bubble_30

        # Validate review dictionary
        review_functions.validate_review(review_dict)

        # Uncomment to print reviews to screen
        review_functions.trip_print_review(review_dict)

        # Uncomment to export results in csv file
        review_functions.trip_export_review(review_dict, page_name)

    # Determine whether we are on the last page
    last_page = False
    next_button_element =  common.find_element_or_default(driver, buttonNext_selector, not_found_flag, wait_time)
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
        common.wait_for_(wait_page_load)
        print( '\n' )


driver.close()