import csv
import re
import time
import datetime
import common

trip_heading = ['Timestamp', 'Titolo', 'Testo', 'Utente - Nome', 'Dispositivo', 'Data', 'Valore', 'Utente - # Rec e Like', 'link', 'Ristorante', 'Sorgente']
face_heading = ['Reviewer Name', 'Date', 'Rating Value', 'Text']
timer = time.time()
timestamp = datetime.datetime.fromtimestamp(timer).strftime('%d-%m-%Y %H:%M:%S')
timestamp_title = datetime.datetime.fromtimestamp(timer).strftime('%d-%m-%Y_%H,%M,%S')

# def get_reviews(url,aggregator):
#     """
#     Takes the URL of the page from which to start scraping reviews.
#     Returns a list of reviews, where each review is represented by
#     a review dictionary.
#     """
#     review_css_selectors = review_functions.css_selectors[aggregator]


def validate_review(review_dict):
    """
    Check if the given review dictionary is correct, return an 
    exception otherwise
    """
    # Validate rating
    rating = review_dict['rating']
    if not common.string_is_integer(rating):
        raise ValueError("Review rating is not a number; value = " + review_dict['rating'])
        
# Create CSV file, add Heading
def trip_setting_csv(page_name):
    file_name = "Trip_" + page_name + "-" + timestamp_title + ".csv"
    file_handler = open(file_name,"+w")
    head = csv.writer(file_handler, delimiter=',',quoting=csv.QUOTE_ALL)
    head.writerow(trip_heading)
    file_handler.close()

# Print Reviews on screen 
def trip_print_review(review_dict):
    print("------------------------------------------------")
    print("Title:      " + review_dict['title'])
    print("Date:       " + review_dict['date'])
    print("Reviewer:   " + review_dict['reviewer_name'])
    print("Device:     " + review_dict['mobile'])
    print("Rating:     " + review_dict['rating'])
    print("Text:       " + review_dict['text'])

# Add Reviews in CSV file
def trip_export_review(review_dict, page_name):
    file_name = "Trip_" + page_name + "-" + timestamp_title + ".csv"
    file_handler = open(file_name,"a")
    trip_export = [timestamp , review_dict['title'], review_dict['text'], review_dict['reviewer_name'], review_dict['mobile'], review_dict['date'], review_dict['rating'], '', '', page_name, 'TripAdvisor']
    trip_out = csv.writer(file_handler, delimiter=',',quoting=csv.QUOTE_ALL)
    trip_out.writerow(trip_export)
    file_handler.close()

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