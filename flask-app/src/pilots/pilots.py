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
    # departure time/airport/gate
    # arrival time/airport/gate
    # plane type
    # Pilot name
    # Copilot name
    # number of people on the plane

    query = '''
            select departureTime,
       departureGate,
       fromCode as fromAirport,
       arrivalTime,
       arrivalGate,
       toCode   as toAirport,
       planeType,
       pilotFirstName,
       pilotLastName,
       coPilotFirstName,
       coPilotLastName,
       numBookings
from (select *
      from (select *
            from (select *
                  from (select *
                        from (select *
                              from Flights f
                                       join
                                   (select p.id as planeID, name as planeType
                                    from Planes p
                                             join PlaneType t on p.type = t.id) c
                                   on f.plane = c.planeID) f
                                 join
                                 (select id as fromId, code as fromCode from Airports) a
                                 on f.fromAirport = a.fromId) f
                           join
                           (select id as toId, code as toCode from Airports) a on f.toAirport = a.toId) f
                     join
                 (select id as pilotId, firstName as pilotFirstName, lastName as pilotLastName from Pilots) p
                 on p.pilotId = f.pilot) f
               join (select id as coPilotId, firstName as coPilotFirstName, lastName as coPilotLastName from Pilots) p
                    on p.coPilotId = f.coPilot) f
         join (select flight as ticketID, count(*) as numBookings from Tickets group by flight) t on f.id = t.ticketID
            '''
    data = execute_query(query)
    return data


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

