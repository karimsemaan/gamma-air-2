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