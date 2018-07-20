## Print to screen the reviews from the given TripAdvisor
## restaurant page, in the following format
## Review's date - Reviewer's name => Rating value


##Review Selector
## id = driver.get_attribute('id')
## date = driver.find_element_by_class_name('ratingDate').get_attribute('title')
## date = datetime.datetime.strptime(date, self.i18n[self.language]['date_format'])
## title = driver.find_element_by_class_name('quote').find_element_by_tag_name('a').find_element_by_class_name('noQuotes').text
## user = driver.find_element_by_class_name('memberOverlayLink').get_attribute('id')
##



# Import Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv


# Webpage to crawl
url = "https://www.tripadvisor.it/Restaurant_Review-g187791-d2321183-Reviews-Sacco_Bistrot-Rome_Lazio.html"
titolo = ".quote a span"
testo = "p.partial_entry"
nome = ".scrname"
mobile = ".viaMobile"
valore = ".review div.rating span.ui_bubble_rating"
data = ".ratingDate"
più = ".ulBlueLinks"
buttonNext = ".next"
risto = input("Quale Ristorante? ")




# Select driver (Chrome Headless)
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#driver = webdriver.Chrome(chrome_options=options)

# Select driver (Chrome Head)
driver = webdriver.Chrome()



# Get URL HTML
driver.get(url)



# wait 6 seconds
time.sleep(6)
# click on the "più" button
driver.find_element_by_css_selector(più).click()
# wait 2 seconds
time.sleep(2)
# get element
rec_title = driver.find_element_by_css_selector(titolo).text
rec_date = driver.find_element_by_css_selector(data).get_attribute('title')
rec_user = driver.find_element_by_class_name('memberOverlayLink').get_attribute('id')
rec_user_name = driver.find_element_by_css_selector(nome).text
rec_text = driver.find_element_by_css_selector(testo).text
rec_mobile = driver.find_element_by_css_selector(mobile).text
rec_valore = driver.find_element_by_css_selector(valore).get_attribute('class')

# wait 2 seconds and click on navigation button
#time.sleep(2)
#driver.find_element_by_css_selector(buttonNext).click()


# Print to screen
print("------------------------")
print(rec_title)
print(rec_date)
print(rec_user_name + '  -  ' + rec_user)
print(rec_mobile)
print("------------------------")
print(rec_valore)
print("------------------------")
print(rec_text)
print("------------------------")

# export results in csv file
export = [rec_user_name,rec_date, rec_title, rec_valore, rec_text,]
out = csv.writer(open(risto+".csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(export)



# Close driver
#time.sleep(5)

driver.close()