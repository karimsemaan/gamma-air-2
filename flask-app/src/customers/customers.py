from flask import Blueprint, request, jsonify, make_response
import json
from src import execute_query


customers = Blueprint('customers', __name__)



# the ones I can think of right now:
# 1) /my-tickets
# 2) /flights
# 3) /ask-questions
@customers.route('/home', methods=['GET'])
def home():
    return '<h1>Customers: Home</h1>'


# TICKETS  #


# Displays all tickets that this customer has booked.
@customers.route('/my-tickets', methods=['GET'])
def my_tickets():
    return '<h1>Customers: My Tickets</h1>'


# BOOKING FLIGHTS #


# Displays all flights available for booking.
# This means finding all non-full flights, as well as maybe having some search parameters
# If we add search parameters to filter, that means modifying this url to include query parameters.
@customers.route('/flights', methods=['GET'])
def see_flights():
    return '<h1>Customers: See all flights</h1>'


# Begins booking process for the given flight ID.
@customers.route('/flights/<flightID>', methods=['GET'])
def see_specific_flight(flightID):
    return '<h1>Customers: See flight #' + flightID + '</h1>'


@customers.route('/get-seat-types')
def get_seat_types():
    # [
    #     {
    #         "label": "Blue",
    #         "value": "BLUE"
    #     },
    #     {
    #         "label": "Green",
    #         "value": "GREEN"
    #     },
    #     {
    #         "label": "Red",
    #         "value": "RED"
    #     }
    # ]
    data = execute_query("select Name from SeatTypes")
    return jsonify([{"label": x, "value": x} for x in data])


# Displays all tickets that this customer has booked
@customers.route('/book-flight/<flightID>', methods=['POST'])
def book_flight(flightID):
    return '<h1>Customers: Submit booking of flight #' + flightID + '</h1>'


# ASKING QUESTIONS #


# Displays a form for the user to submit a question (with optional fields to attach it to a flight
# or to a pilot or whatever else is in the DB cuz I forget).
# When submitting the form on this page, hits the '/submit-question?...' route with the information
@customers.route('/ask-questions', methods=['GET'])
def ask_question():
    return '<h1>Customers: Ask a question</h1>'


# Adds a question to the DB, using the given parameters to fill out the tuple.
# Once done, redirects back to the home page.
# Parameters:
# 1) questionText -> the text of the question being asked
# 2) flightID/pilotID/airlineID -> -1 if not attached, otherwise an ID of that entity to attach to this question.
@customers.route(
    '/submit-question?question=<questionText>&flight=<flightID>&pilot=<pilotID>&airline=<airlineID>',
    methods=['GET'])
def submit_question(questionText, flightID, pilotID, airlineID):
    return '<h1>Customers: Submitting question</h1>'


# REVIEWS #


# Displays a form to fill out a review of a flight (using the given flightID).
# Once submitted, redirects to the '/submit-review?...' route with the appropriate parameters.
@customers.route('/add-review/<flightID>', methods=['GET'])
def add_review(flightID):
    return '<h1>Customers: Add a review of flight #' + flightID + '</h1>'


# Adds a review on the given flight ID to the DB, using the given parameters to fill out the tuple.
# Once done, redirects back to the home page.
# Parameters:
# 1) description -> the text of the review being given
# 2) score -> a number 1..5 (inclusive) scoring the flight overall.
@customers.route('/submit-question/<flightID>?description=<description>&score=<score>', methods=['GET'])
def submit_review(flightID, description, score):
    return '<h1>Customers: Submitting new review</h1>'

