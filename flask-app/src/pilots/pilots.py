from flask import Blueprint
from src import execute_query
from src.log_in import current_user_id

pilots = Blueprint('pilots', __name__)


@pilots.route('/home', methods=['GET'])
def home():
    return '<h1>Pilots: Home</h1>'


# SCHEDULES


# Display's the pilot's current schedule
@pilots.route('/schedule', methods=['GET'])
def schedule():
    query_time = '''select departureTime, arrivalTime
    from Flights
    where Flights.coPilot = {0} or Flights.pilot = {0}
    order by departureTime'''.format(current_user_id)
    data_time = execute_query(query_time)

    query_airport = '''select name 
    from Airport natural join (select * from Flights
    where Flights.coPilot = {0} or Flights.pilot = {0}) as pilotFlights
    where Airports.id = pilotFlights.fromAirport or Airports.id = pilotFlights.toAirport'''.format(current_user_id)
    data_airport = execute_query(query_airport)
    return data_time, data_airport


# allows the pilot to submit a rescheduling request
@pilots.route('/schedule/change-schedule/<flightID>', methods=['POST'])
def schedule_change_flight(flightID):
    return '<h1>Pilots: Submit schedule change request for flight #' + flightID + '</h1>'


# REVIEWS


# displays all the reviews of all the flights
# this pilot has been responsible for
@pilots.route('/my-reviews', methods=['GET'])
def pilot_reviews():
    query = ''' select * from 
            (select * from CustomerRep where id = {}) natural join Reviews
            '''
    data = execute_query(query.format(current_user_id))
    return '<h1>Pilots: My Reviews<h1>'

