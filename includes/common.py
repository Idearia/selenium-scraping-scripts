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

def string_is_integer(s):
    """

    """
    try: 
        int(s)
        return True
    except ValueError:
        return False
