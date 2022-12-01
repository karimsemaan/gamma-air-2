from flask import Blueprint, request, jsonify, make_response
import json
from src import db


reps = Blueprint('reps', __name__)


# contains buttons to redirect to all main (top level) pages for representatives
# the ones I can think of right now:
# 1) /matching-pilots-flights
# 2) /answer-questions
@reps.route('/home', methods=['GET'])
def home():
    return '<h1>Representatives: Home</h1>'


# MATCHING FLIGHTS AND PILOTS #


# displays a view allowing the user to select a pilot and a flight
# assigning that pilot to that flight.
# this means getting all flights that are unassigned, and then all pilots.
# A pilot can be assigned to either pilot or copilot a flight.
# When this is done, it hits the endpoint in this file at '/matching' with the appropriate query parameters
@reps.route('/matching-pilots-flights', methods=['GET'])
def assign_pilots():
    return '<h1>Representatives: Assign Pilots to Flights</h1>'


# this endpoint might break right now, since it is a POST but has code inside it as if it were a GET (returning)
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
@reps.route('/answer-questions', methods=['GET'])
def answer_questions():
    return '<h1>Representatives: View asked questions</h1>'


# might not work also since POST
# Submits an answer to the database and redirects back to the '/answer-questions' route.
@reps.route('/submit-answer/<questionID>?response=<responseText>', methods=['POST'])
def assign_pilots(questionID, responseText):
    return '<h1>Representatives: Answering question # ' + questionID + '</h1>'

