import csv
import re
import time

#localtime = time.asctime(time.localtime(time.time()))
trip_heading = ['Reviewer Name', 'Date', 'Title', 'Rating Value', 'Text', 'Via Mobile']
face_heading = ['Reviewer Name', 'Date', 'Rating Value', 'Text']

def find_element_text_or_default(parent_element, css_selector, default_value="NOT FOUND"):
    """Find an element via a CSS selector and extract its text
    Returns the default value if the elmenent cannot be found.
    """
    output = default_value # initialize output 
    try: # try to get element
        output = parent_element.find_element_by_css_selector(css_selector).text
    except:
        pass
    return output

def find_element_attribute_or_default(parent_element, css_selector, attribute, default_value="NOT FOUND"):
    """Find an element via a CSS selector and extract the content of one of its attributes
    Returns the default value if the elmenent cannot be found.
    """
    output = default_value # initialize output 
    try: # try to get element
        output = parent_element.find_element_by_css_selector(css_selector).get_attribute(attribute)
    except:
        pass
    return output



# Tripadvisor output
def trip_setting_csv(page_name):
    head = csv.writer(open("Trip_" + page_name + ".csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
    head.writerow(trip_heading)    

def trip_print_review(title, date, reviewer_name, text, mobile, rating_value):
    print("------------------------------------------------")
    print("Title:      " + title)
    print("Date:       " + date)
    print("Reviewer:   " + reviewer_name)
    print("Device: " + mobile)
    print("Rating:     " + rating_value)
    print("Text:       " + text)

def trip_export_review(reviewer_name,date, title, rating_value, text, mobile, page_name):
    trip_export = [reviewer_name,date, title, rating_value, text, mobile]
    trip_out = csv.writer(open("Trip_" + page_name + ".csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
    trip_out.writerow(trip_export)





# Facebook output
def face_setting_csv(page_name):
    head = csv.writer(open("Face_" + page_name + ".csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
    head.writerow(face_heading) 

def face_print_review(reviewer_name, date, rating_value, text):
    print("------------------------------------------------")
    print("Reviewer:   " + reviewer_name)
    print("Date:       " + date)
    print("Rating:     " + rating_value)
    print("Text:       " + text)

def face_export_review(reviewer_name, date, rating_value, text, page_name):
    face_export = [reviewer_name, date, rating_value, text]
    face_out = csv.writer(open("Face_" + page_name + ".csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
    face_out.writerow(face_export)    