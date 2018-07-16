# Import Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Select Chrome Headless Driver
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

# Run the test as described in
# https://blog.michaelyin.info/web-scraping-framework-review-scrapy-vs-selenium/
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title
driver.close()