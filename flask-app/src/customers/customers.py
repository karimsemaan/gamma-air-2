from flask import Blueprint, request, jsonify
from src import execute_query, get_next_id
from src.log_in import current_user_id


customers = Blueprint('customers', __name__)


# TICKETS  #


# Displays all tickets that this customer has booked.
@customers.route('/my-tickets', methods=['GET'])
def my_tickets():
    query = '''select * from Tickets
        where customer = {}
        '''
    data = execute_query(query.format('7586001'))

    # [
    #  { "Airline" : airline name,
    #    "From" : flight from, departure time,
    #    "To" : flight to, arrival time,
    #    "SeatType" : flight seatType
    #  },
    #  {...}
    # ]
    return jsonify(data)


# BOOKING FLIGHTS #


@customers.route('/get-seat-types')
def get_seat_types():
    data = execute_query("select id as value, name as label from SeatTypes")
    return jsonify(data)


# ASKING QUESTIONS #


# Adds a question to the DB, using the given parameters to fill out the tuple.
# Once done, redirects back to the home page.

# ROUTE NOT COMPLETE:
# - how do you generate a unique question ID
# - how do you fill in the cust ID and cust_rep ID fields of the table?

@customers.route('/submit-question/', methods=['POST'])
def submit_question():
    id = get_next_id('Questions')
    args = request.args.to_dict()  # questionText, flightID, pilotID, airlineID
    question = args.get("question")
    flight = args.get("flightID")
    pilot = args.get("pilotID")
    airline = args.get("airlineID")
    query = '''INSERT INTO Questions(id, question, isResolved, customer, flight, pilot, airline)
               VALUES({0}, {1}, false, {2}, {3}, {4}, {5})
               '''.format(id, question, current_user_id, flight, pilot, airline)
    execute_query(query)


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

