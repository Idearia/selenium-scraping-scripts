import time

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

def wait_for_page_load():
    """
    Wait enough time for a Trip Advisor page to load 
    """
    time.sleep(6)

def element_is_disabled(element):
    """
    Check if the given Selenium element has the 'disabled' class
    TODO: Use split+in_array find instead of substring find. 
    """
    disabled = False
    if 'disabled' in element.get_attribute('class'):
        disabled = True
    return disabled

def string_is_integer(s):
    """

    """
    try: 
        int(s)
        return True
    except ValueError:
        return False
