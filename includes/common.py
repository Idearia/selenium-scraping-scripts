import csv

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

def print_review(title, date, reviewer_name, text, mobile, rating_value):
    print("------------------------------------------------")
    print("Title:      " + title)
    print("Date:       " + date)
    print("Reviewer:   " + reviewer_name)
    print("Device: " + mobile)
    print("Rating:     " + rating_value)
    print("Text:       " + text)

def export_review(reviewer_name,date, title, rating_value, text, mobile):
    export = [reviewer_name,date, title, rating_value, text, mobile]
    out = csv.writer(open("Scrape.csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(export)