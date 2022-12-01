from flask import Blueprint
import json
from src import db

pilots = Blueprint('pilots', __name__)


@pilots.route('/home', methods=['GET'])
def home():
    return '<h1>Pilots: Home</h1>'

# SCHEDULES

# Display's the pilot's current schedule

# allows the pilot to submit rescheduling requests


# REVIEWS


# displays all the reviews of all the flights
# this pilot has been responsible for
@pilots.route('/my-reviews', methods=['GET'])
def pilot_reviews():
    return '<h1>Pilots: My Reviews<h1>'

