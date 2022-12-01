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

# allows the pilot to view reviews of the flights they have been responsible for