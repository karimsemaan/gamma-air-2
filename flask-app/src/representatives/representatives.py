from flask import Blueprint, request, jsonify, current_app
from src import execute_query
import src.log_in as user_info

reps = Blueprint('reps', __name__)


# MATCHING FLIGHTS AND PILOTS #


# Displays a view allowing the user to select a pilot and a flight
# assigning that pilot to that flight.
# This means getting all flights that are unassigned, and then all pilots.
# A pilot can be assigned to either pilot or copilot a flight.
# When this is done, it hits the endpoint in this file at '/matching' with the appropriate query parameters
@reps.route('/matching-pilots-flights', methods=['GET'])
def assign_pilots():
    return '<h1>Representatives: Assign Pilots to Flights</h1>'


# This endpoint might break right now, since it is a POST but has code inside it as if it were a GET (returning)
#
# This endpoint is responsible for assigning a pilot to a flight. It has three parameters:
# 1) the pilot ID (the pilot to assign to the given flight)
# 2) the flight ID (the flight to assign the given pilot to)
# 3) isCopilot, a boolean that - if true - means the given pilotID should be assigned as a copilot for this flight
#   if false, it assigns the given pilot as pilot.
@reps.route('/matching?pilot=<pilotID>&flight=<flightID>&isCopilot=<isCopilot>', methods=['POST'])
def match_pilot(pilotID, flightID, isCopilot):
    type = 'Copilot' if isCopilot else 'Pilot'
    return '<h1>Representatives: Assigning ' + type + ' ID #' + pilotID + 'to Flight ID #' + flightID + '</h1>'


# ANSWERING QUESTIONS #


# Displays all questions asked by customers that this representative is assigned to.
# Doesn't display questions that are already answered.
@reps.route('/view-questions', methods=['GET'])
def view_questions():
    query = '''select id, question, isResolved from 
        (select id as customer from Customers where supportRep = {0}) c natural join Questions
        order by isResolved
        '''
    data = execute_query(query.format(user_info.current_user_id))
    return jsonify(data)


@reps.route('/view-question/<questionID>', methods=['GET'])
def view_specific_question(questionID):
    query = '''select question, response, firstName, lastName, f.id as flightId, name as airlineName
        from Questions q join Customers c on q.customer = c.id
        join Flights f on f.id = q.flight
        join Airlines a on a.id = q.airline
        where q.id = {}'''

    data = execute_query(query.format(questionID))

    return data


# Submits an answer to the database and redirects back to the '/answer-questions' route.
@reps.route('/submit-answer/<questionID>', methods=['POST'])
def submit_answer(questionID):
    response = request.args.to_dict().get("response")
    query = '''update Questions 
        set response = {0}, isResolved = true, customerRep = {1}
        where id = {2}
        '''.format(response, user_info.current_user_id, questionID)
    execute_query(query)
