from flask import Blueprint

from src import execute_query
from src.log_in import current_user_id

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
    query = ''' select * from
            (select * from CustomerRep where id = {}) natural join Questions
            '''
    data = execute_query(query.format(current_user_id))
    return '<h1>Representatives: View asked questions</h1>'


# Might not work also since POST
# Submits an answer to the database and redirects back to the '/answer-questions' route.
@reps.route('/submit-answer/<questionID>?response=<responseText>', methods=['POST'])
def submit_answer(questionID, responseText):
    return '<h1>Representatives: Answering question #' + questionID + '</h1>'

