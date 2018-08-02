import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def find_elements_or_default(parent_element, css_selector, default_value="NOT FOUND", wait_time = 20):
    """Find elements via a CSS selector and return them as a list.
    If not found, return the default_value argument.
    """
    elements = default_value # initialize output 
    try:
        elements = WebDriverWait(parent_element, wait_time).until(
            EC.presence_of_all_elements_located(('css', css_selector))
        )
    except:
        # Uncomment to throw an error
        # raise NameError("Element: " + css_selector + " not found")
        pass
    return elements

def find_element_or_default(parent_element, css_selector, default_value="NOT FOUND", wait_time = 20):
    """Find an element via a CSS selector and return it.
    If not found, return the default_value argument.
    """
    element = default_value # initialize output 
    try:
        element = WebDriverWait(parent_element, wait_time).until(
            EC.presence_of_element_located(('css', css_selector))
        )
    except:
        # Uncomment to throw an error
        # raise NameError("Element: " + css_selector + " not found")
        pass
    return element

def find_element_text_or_default(parent_element, css_selector, default_value="NOT FOUND", wait_time = 20):
    """Find an element via a CSS selector and return its text.
    Return the default value if the element cannot be found.
    """
    element = find_element_or_default(parent_element, css_selector, default_value, wait_time)
    if element is default_value:
        return default_value
    else:
        return element.text

def find_element_attribute_or_default(parent_element, css_selector, attribute, default_value="NOT FOUND", wait_time = 20):
    """Find an element via a CSS selector and return the value of the given attribute.
    Return the default value if the element cannot be found.
    """
    element = find_element_or_default(parent_element, css_selector, default_value, wait_time)
    if element is default_value:
        return default_value
    else:
        return element.get_attribute(attribute)

def wait_for_(wait_time = 20):
    """
    Wait enough time for a Trip Advisor page to load 
    """
    time.sleep(wait_time)
    # pass

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
    Check if the given string contain an integer
    """
    try: 
        int(s)
        return True
    except ValueError:
        return False

def click_button(parent, css_selector):
    """
    Check if there is a button and if it is clickable, click it
    Return True if the button was clicked, False otherwise
    """
    output = False
    try:
        button = parent.find_element_by_css_selector(css_selector)
        if button.is_enabled():
            button.click()
            output = True
    # Ok if the button does not exist: go ahead
    except:
        pass
    return output    