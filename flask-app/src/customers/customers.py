from flask import Blueprint, request, jsonify, current_app
from src import execute_query, get_next_id
import src.log_in as user_info


customers = Blueprint('customers', __name__)


# TICKETS  #


# Displays all tickets that this customer has booked.
@customers.route('/my-tickets', methods=['GET'])
def my_tickets():
    query = '''
    select departureGate,
       departureTime,
       fromCode    as fromAirport,
       arrivalGate,
       arrivalTime,
       toCode      as toAirport,
       ST.name     as seatType,
       accommodations,
       insuredTrip,
       hasDisability,
       airlineName as airline
from Tickets
         join SeatTypes ST on Tickets.seatType = ST.id
         join Flights F on Tickets.flight = F.id
         join Planes P on F.plane = P.id
         join (select id, name as airlineName from Airlines) A on P.airline = A.id
         join (select id as fromId, code as fromCode from Airports) A2 on A2.fromId = F.fromAirport
         join (select id as toId, code as toCode from Airports) A3 on A3.toId = F.toAirport
where customer = {}
        '''
    data = execute_query(query.format(user_info.current_user_id))
    return jsonify(data)


# BOOKING FLIGHTS #


@customers.route('/get-seat-types')
def get_seat_types():
    data = execute_query("select id as value, name as label from SeatTypes")
    return jsonify(data)


# ASKING QUESTIONS #


# Adds a question to the DB, using the given parameters to fill out the tuple.
# Once done, redirects back to the home page.
@customers.route('/submit-question', methods=['POST'])
def submit_question():
    question_id = get_next_id('Questions')
    args = request.args.to_dict()  # questionText, flightID, pilotID, airlineID
    question = args.get("question").replace("'", "\\'").replace('"', '\\"')
    flight = args.get("flightID", 'null')
    pilot = args.get("pilotID", 'null')
    airline = args.get("airlineID", 'null')
    current_app.logger.info(user_info.current_user_id)
    query = '''INSERT INTO Questions(id, question, isResolved, customer, flight, pilot, airline)
               VALUES({0}, '{1}', false, {2}, {3}, {4}, {5})
               '''.format(question_id, question, user_info.current_user_id, flight, pilot, airline)
    current_app.logger.info(query)
    execute_query(query, True)
    return 'Success'
