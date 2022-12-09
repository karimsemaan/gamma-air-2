from flask import Blueprint, request, jsonify
from src import execute_query
from src.log_in import current_user_id


customers = Blueprint('customers', __name__)


# TICKETS  #


# Displays all tickets that this customer has booked.
@customers.route('/my-tickets', methods=['GET'])
def my_tickets():
    query = '''select * from 
        (select * from Customers where id == {}) natural join Tickets
        '''
    data = execute_query(query.format(current_user_id))
    return '<h1>Customers: My Tickets</h1>'


# BOOKING FLIGHTS #


@customers.route('/get-seat-types')
def get_seat_types():
    data = execute_query("select id as value, name as label from SeatTypes")
    return jsonify(data)


# ASKING QUESTIONS #


# Adds a question to the DB, using the given parameters to fill out the tuple.
# Once done, redirects back to the home page.
# Parameters:
# 1) questionText -> the text of the question being asked
# 2) flightID/pilotID/airlineID -> -1 if not attached, otherwise an ID of that entity to attach to this question.
@customers.route(
    '/submit-question',
    methods=['GET'])
def submit_question():
    args = request.args  # questionText, flightID, pilotID, airlineID
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
@customers.route('/submit-question/<flightID>', methods=['GET'])
def submit_review(flightID):
    args = request.args  # description, score
    return '<h1>Customers: Submitting new review</h1>'

