import csv
import re
import time
import datetime
import common
import pandas as pd

trip_heading = ['Timestamp', 'Titolo', 'Testo', 'Utente - Nome', 'Dispositivo', 'Data', 'Valore', 'Utente - # Rec e Like', 'link', 'Ristorante', 'Sorgente']
face_heading = ['Reviewer Name', 'Date', 'Rating Value', 'Text']
timer = time.time()
timestamp = datetime.datetime.fromtimestamp(timer).strftime('%d-%m-%Y %H:%M:%S')

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
    file_name = "Trip_" + page_name + ".csv"
    file_handler = open(file_name,"+w")
    head = csv.writer(file_handler, delimiter=',',quoting=csv.QUOTE_ALL)
    head.writerow(trip_heading)
    file_handler.close()

# Print Reviews on screen 
def trip_print_review(review_dict):
    print("Title:      " + review_dict['title'])
    print("Date:       " + review_dict['date'])
    print("Reviewer:   " + review_dict['reviewer_name'])
    print("Device:     " + review_dict['mobile'])
    print("Rating:     " + review_dict['rating'])
    print("Text:       " + review_dict['text'])

# Add Reviews in CSV file
def trip_export_review(review_dict, page_name):
    file_name = "Trip_" + page_name + ".csv"
    file_handler = open(file_name,"a")
    trip_export = [timestamp , review_dict['title'], review_dict['text'], review_dict['reviewer_name'], review_dict['mobile'], review_dict['date'], review_dict['rating'], '', '', page_name, 'TripAdvisor']
    trip_out = csv.writer(file_handler, delimiter=',',quoting=csv.QUOTE_ALL)
    trip_out.writerow(trip_export)
    file_handler.close()

# Read date from last scrape
# def read_date(page_name):
#     dict = {}
#     dict['gennaio'] = '1'
#     dict['febraio'] = '2'
#     dict['marzo'] = '3'
#     dict['aprile'] = '4'
#     dict['maggio'] = '5'
#     dict['giugno'] = '6'
#     dict['luglio'] = '7'
#     dict['agosto'] = '8'
#     dict['settembre'] = '9'
#     dict['ottobre'] = '10'
#     dict['novembre'] = '11'
#     dict['dicembre'] = '12'
    
#     file_name = "Trip_" + page_name + ".csv"
#     date = pd.read_csv(file_name)
#     date['Data'] = pd.to_datetime(dict, format="%d %m %Y")
#     print(date['Data'])

# # Facebook output
# def face_setting_csv(page_name):
#     head = csv.writer(open("Face_" + page_name + ".csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
#     head.writerow(face_heading) 

# def face_print_review(reviewer_name, date, rating_value, text):
#     print("------------------------------------------------")
#     print("Reviewer:   " + reviewer_name)
#     print("Date:       " + date)
#     print("Rating:     " + rating_value)
#     print("Text:       " + text)

# def face_export_review(reviewer_name, date, rating_value, text, page_name):
#     face_export = [reviewer_name, date, rating_value, text]
#     face_out = csv.writer(open("Face_" + page_name + ".csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
#     face_out.writerow(face_export)    