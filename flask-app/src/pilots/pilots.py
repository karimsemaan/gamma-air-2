from flask import Blueprint, jsonify, current_app
from src import execute_query
import src.log_in as user_info

pilots = Blueprint('pilots', __name__)


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
from (select * from Flights where pilot = {0} or coPilot = {0}) f
         join (select id as planeId, type from Planes) pl on pl.planeId = f.plane
         join (select id as planeTypeId, name as planeType from PlaneType) pt on pt.planeTypeId = pl.type
         join (select id as toId, code as toCode from Airports) a1 on a1.toId = f.toAirport
         join (select id as fromId, code as fromCode from Airports) a2 on a2.fromId = f.fromAirport
         join (select id as pilotId, firstName as pilotFirstName, lastName as pilotLastName from Pilots) p1
              on p1.pilotId = f.pilot
         join (select id as coPilotId, firstName as coPilotFirstName, lastName as coPilotLastName from Pilots) p2
              on p2.coPilotId = f.coPilot
         join (select flight as ticketID, count(*) as numBookings from Tickets group by flight) t on f.id = t.ticketID
            '''.format(user_info.current_user_id)
    data = execute_query(query)
    return data


# REVIEWS


# displays all the reviews of all the flights
# this pilot has been responsible for
@pilots.route('/my-reviews', methods=['GET'])
def pilot_reviews():
    query = '''
    select
        C.firstName   as firstName,
        C.lastName    as lastName,
        F.id          as flightId,
        R.description as description,
        R.score       as score
    from Pilots
             join Flights F on Pilots.id = F.pilot or Pilots.id = F.coPilot
             join Reviews R on F.id = R.flight
             join Customers C on R.customer = C.id
    where Pilots.id = {}
            '''
    current_app.logger.info(user_info.current_user_id)
    data = execute_query(query.format(user_info.current_user_id))
    return jsonify(data)

