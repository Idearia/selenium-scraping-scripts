## Print to screen the reviews from the given TripAdvisor
## restaurant page, in the following format
## Review's date - Reviewer's name => Rating value

# Import Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Webpage to crawl
url = "https://www.tripadvisor.it/Restaurant_Review-g187791-d2321183-Reviews-Sacco_Bistrot-Rome_Lazio.html"

# Select driver (Chrome Headless)
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

# Get URL HTML

# Get elements

# Extract reviews from elements

# Check extraction results

# Print to screent

# Close driver
driver.close()