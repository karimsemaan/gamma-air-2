from flask import Blueprint
import json
from src import db

pilots = Blueprint('pilots', __name__)


@pilots.route('/home', methods=['GET'])
def home():
    return '<h1>Pilots: Home</h1>'


# SCHEDULES


# Display's the pilot's current schedule
@pilots.route('/schedule', methods=['GET'])
def schedule():
    return '<h1>Pilots: My Schedule</h1>'


# allows the pilot to submit a rescheduling request
@pilots.route('/change-schedule/<flightID>', methods=['POST'])
def schedule_change_flight(flightID):
    return '<h1>Pilots: Submit schedule change request for flight #' + flightID + '</h1>'


# REVIEWS


# displays all the reviews of all the flights
# this pilot has been responsible for
@pilots.route('/my-reviews', methods=['GET'])
def pilot_reviews():
    return '<h1>Pilots: My Reviews<h1>'

