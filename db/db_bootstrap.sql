create database GammaAir;

create user 'root_user'@'%' identified by 'abc123';
grant all privileges on GammaAir.* to 'root_user'@'%';
flush privileges;

create user 'webapp'@'%' identified by 'abc1234';
grant all privileges on GammaAir.* to 'webapp'@'%';
flush privileges;

use GammaAir;

create table CustomerRep (
   id int,
   salary float,
   firstName varchar(50),
   lastName varchar(50),
   managerId int,
   primary key (id),
   foreign key (managerId) references CustomerRep(id)
);

create table Customers (
   id int,
   firstName varchar(50),
   lastName varchar(50),
   email varchar(50),
   supportRep int, -- designatedCustRep -> supportRep
   primary key (id),
   foreign key (supportRep) references CustomerRep(id)
);

create table Pilots (
   id int,
   firstName varchar(50),
   lastName varchar(50),
   experience int,
   hourlyRate int,
   primary key (id)
);

create table Airlines (
   id int,
   name varchar(50),
   email varchar(50),
   managerPhone varchar(50),
   starRating int,
   additionalBagCost int,
   primary key (id)
);

create table Airports (
   id int,
   name varchar(50),
   code varchar(50),
   country varchar(50),
   state varchar(50),
   city varchar(50),
   primary key (id)
);

create table PlaneType (
   id int,
   name varchar(50),
   primary key (id)
);

create table Planes (
   id int,
   maxLuggageWeight int,
   maxDistance int,
   disabilityAccess boolean,
   type int,
   airline int,
   primary key (id),
   foreign key (type) references PlaneType(id),
   foreign key (airline) references Airlines(id)
);

create table SeatTypes (
   id int,
   name varchar(50),
   additionalSeatCost int,
   primary key (id)
);

create table PlaneSeats (
   id int,
   seatType int,
   plane int,
   availabilityNumber int,
   primary key (id),
   foreign key (seatType) references SeatTypes(id),
   foreign key (plane) references Planes(id)
);

create table Flights (
   id int,
   baseCost int,
   departureTime datetime,
   arrivalTime datetime,
   cancelled boolean,
   arrivalGate varchar(100),
   departureGate varchar(100),
   fromAirport int,
   toAirport int,
   plane int,
   pilot int,
   coPilot int,
   primary key (id),
   foreign key (fromAirport) references Airports(id),
   foreign key (toAirport) references Airports(id),
   foreign key (plane) references Planes(id),
   foreign key (pilot) references Pilots(id),
   foreign key (coPilot) references Pilots(id)
);

create table ScheduleRequests (
   reason varchar(1000),
   pilot int,
   flight int,
   primary key (pilot, flight),
   foreign key (pilot) references Pilots(id),
   foreign key (flight) references Flights(id)
);

create table Reviews (
   customer int,
   flight int,
   description varchar(1000),
   score int,
   primary key (customer, flight),
   foreign key (customer) references Customers(id),
   foreign key (flight) references Flights(id)
);

create table Tickets (
   id int,
   customer int,
   flight int,
   seatType int,
   accommodations varchar(1000),
   insuredTrip boolean,
   hasDisability boolean,
   checkedBaggageWeight int,
   primary key (id),
   foreign key (customer) references Customers(id),
   foreign key (flight) references Flights(id),
   foreign key (seatType) references SeatTypes(id)
);

create table Questions (
   id int,
   question varchar(1000),
   response varchar(1000),
   isResolved boolean,
   customer int,
   customerRep int,
   flight int, -- optional tags for the question if the user wants
   pilot int, -- optional tags for the question if the user wants
   airline int, -- optional tags for the question if the user wants
   primary key (id),
   foreign key (customer) references Customers(id),
   foreign key (customerRep) references CustomerRep(id),
   foreign key (flight) references Flights(id),
   foreign key (pilot) references Pilots(id),
   foreign key (airline) references Airlines(id)
);

use GammaAir;

insert into CustomerRep (id, salary, firstName, lastName, managerId) values (3428687, 51670.55, 'Urbanus', 'Gravells', 3428687);

insert into CustomerRep (id, salary, firstName, lastName, managerId) values (5240615, 46189.40, 'Izabel', 'Nanelli', 3428687);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (0968870, 37247.70, 'Shurwood', 'Machel', 3428687);

insert into CustomerRep (id, salary, firstName, lastName, managerId) values (1550028, 53927.96, 'Dorie', 'Gilliland', 5240615);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (9113258, 37610.56, 'Colleen', 'Edney', 5240615);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (2211276, 32957.30, 'Kellen', 'Pickervance', 5240615);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (7190305, 33653.38, 'Robbie', 'Ghidoli', 5240615);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (1330501, 54435.70, 'Sim', 'Hammill', 0968870);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (0087498, 30069.20, 'Barnaby', 'Agerskow', 0968870);
insert into CustomerRep (id, salary, firstName, lastName, managerId) values (2346794, 53881.28, 'Kilian', 'Abrahmovici', 0968870);

-- Generating data for Customers:
use GammaAir;

insert into Customers (id, firstName, lastName, email, supportRep)
values (7586001, 'Caryl', 'Neely', 'cneely0@cafepress.com', 1330501);
insert into Customers (id, firstName, lastName, email, supportRep)
values (6567114, 'Winthrop', 'Ronca', 'wronca1@bbc.co.uk', 0087498);
insert into Customers (id, firstName, lastName, email, supportRep)
values (5928192, 'Garfield', 'Driffill', 'gdriffill2@msn.com', 2346794);
insert into Customers (id, firstName, lastName, email, supportRep)
values (2943577, 'Georgie', 'Ranfield', 'granfield3@symantec.com', 2346794);
insert into Customers (id, firstName, lastName, email, supportRep)
values (5104420, 'Kincaid', 'Janjic', 'kjanjic4@baidu.com', 2346794);
insert into Customers (id, firstName, lastName, email, supportRep)
values (3935181, 'Gretel', 'Offa', 'goffa5@usnews.com', 0087498);
insert into Customers (id, firstName, lastName, email, supportRep)
values (6227087, 'Cecily', 'Dowbakin', 'cdowbakin6@ox.ac.uk', 0087498);
insert into Customers (id, firstName, lastName, email, supportRep)
values (3696313, 'Dore', 'Neggrini', 'dneggrini7@1688.com', 1330501);
insert into Customers (id, firstName, lastName, email, supportRep)
values (3232291, 'Eunice', 'MacKey', 'emackey8@msu.edu', 3428687);
insert into Customers (id, firstName, lastName, email, supportRep)
values (1894155, 'Barrie', 'Durham', 'bdurham9@ifeng.com', 3428687);

-- Generating data for Pilots:
use GammaAir;

insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (0, 'Hollyanne', 'Docherty', 5, 80);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (1, 'Thoma', 'Bettridge', 3, 60);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (2, 'Melissa', 'Ettridge', 4, 80);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (3, 'Sammie', 'Scala', 2, 79);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (4, 'Bondy', 'Heggison', 4, 76);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (5, 'Dalis', 'Millard', 3, 61);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (6, 'Farrel', 'Ledner', 4, 60);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (7, 'Oswell', 'Mate', 3, 73);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (8, 'Natale', 'Ends', 3, 60);
insert into Pilots (id, firstName, lastName, experience, hourlyRate) values (9, 'Tony', 'Wilsdon', 2, 62);

-- Generating data for Airlines:
use GammaAir;

insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (1465692, 'Qatar Airways', 'dqwelcomehome@qatarairways.com.qa', '742-468-4388', 5, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (0160829, 'Singapore Airlines', 'welcomehome@singaporeairlines.com.sa', '937-953-3068', 5, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (1013398, 'Emirates', 'welcomehome@emirates.com.e', '769-985-1960', 2, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (8282010, 'ANA', 'welcomehome@ana.com.ana', '392-531-5479', 4, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (8673333, 'Qantas Airways', 'welcomehome@quantasairways.com.qa', '150-480-6677', 1, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (4468710, 'Japan Airlines', 'welcomehome@japanairlines.com.ja', '937-909-8338', 3, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (2118212, 'Turkish Airlines', 'welcomehome@turkishairlines.com.ta', '785-299-2602', 4, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (0948593, 'Air France', 'welcomehome@airfrance.com.af', '786-359-6030', 1, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (8175898, 'Korean Air', 'welcomehome@koreanair.com.ka', '527-289-2361', 4, 20);
insert into Airlines (id, name, email, managerPhone, starRating, additionalBagCost)
values (8427218, 'Swiss International Air Lines', 'welcomehome@swissinternationalairlines.com.sial', '510-687-6757', 2, 20);

-- Generating data for Airports:
use GammaAir;

insert into Airports (id, name, code, country, state, city) values (0, 'Montgomery Regional (Dannelly Field) Airport', 'MGM', 'Pakistan', null, 'Qādirpur Rān');
insert into Airports (id, name, code, country, state, city) values (1, 'Yantai Penglai International Airport', 'YNT', 'China', 'Shandong', 'Yantai');
insert into Airports (id, name, code, country, state, city) values (2, 'Kuressaare Airport', 'URE', 'Sweden', 'Gävleborg', 'Sandviken');
insert into Airports (id, name, code, country, state, city) values (3, 'Amarais Airport', 'CPQ', 'Finland', null, 'Tuupovaara');
insert into Airports (id, name, code, country, state, city) values (4, 'Captain Jack Thomas El Dorado Airport', 'EDK', 'United States', 'Colorado', 'Colorado Springs');
insert into Airports (id, name, code, country, state, city) values (5, 'Po Airport', 'PUP', 'Japan', null, 'Sakata');
insert into Airports (id, name, code, country, state, city) values (6, 'Casement Airport', 'PVZ', 'Poland', null, 'Kamionka Wielka');
insert into Airports (id, name, code, country, state, city) values (7, 'Sapmanga Airport', 'SMH', 'Japan', null, 'Nagano-shi');
insert into Airports (id, name, code, country, state, city) values (8, 'Alberto Delgado Airport', 'TND', 'Uzbekistan', null, 'Yangirabot');
insert into Airports (id, name, code, country, state, city) values (9, 'Muscatine Municipal Airport', 'MUT', 'Slovenia', null, 'Dob');

-- Generating data for PlaneType:
use GammaAir;

insert into PlaneType (id, name) values (0, 'Airbus A380');
insert into PlaneType (id, name) values (1, 'Boeing 747-8');
insert into PlaneType (id, name) values (2, 'Boeing 777-9');
insert into PlaneType (id, name) values (3, 'Antonov An-124');
insert into PlaneType (id, name) values (4, 'Lockheed C-5 Galaxy');
insert into PlaneType (id, name) values (5, 'Airbus Beluga XL');
insert into PlaneType (id, name) values (6, 'Boeing Dreamlifter');
insert into PlaneType (id, name) values (7, 'Hughes H-4 Hercules');
insert into PlaneType (id, name) values (8, 'Stratolaunch');
insert into PlaneType (id, name) values (9, 'Airbus A330');

-- Generating data for Planes:
use GammaAir;

insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (0, 485, 2418, false, 4, 1465692);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (1, 127, 4865, true, 1, 1013398);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (2, 113, 5871, false, 1, 1013398);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (3, 238, 5972, false, 4, 2118212);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (4, 742, 7056, true, 4, 2118212);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (5, 540, 4273, true, 5, 1465692);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (6, 178, 5202, false, 1, 1465692);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (7, 185, 4133, true, 5, 1013398);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (8, 683, 3744, false, 1, 2118212);
insert into Planes (id, maxLuggageWeight, maxDistance, disabilityAccess, type, airline) values (9, 371, 4587, false, 4, 2118212);

-- Generating data for SeatTypes:

insert into SeatTypes (id, name, additionalSeatCost) values (0, 'Economy', 0);
insert into SeatTypes (id, name, additionalSeatCost) values (1, 'Business', 336);
insert into SeatTypes (id, name, additionalSeatCost) values (2, 'First-Class', 544);

-- Generating data for PlaneSeats:
use GammaAir;

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (0, 0, 0, 100);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (1, 2, 0, 20);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (2, 1, 0, 50);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (3, 0, 1, 5);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (4, 2, 1, 60);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (5, 0, 2, 20);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (6, 2, 2, 200);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (7, 0, 3, 16);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (8, 1, 3, 75);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (9, 2, 3, 15);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (10, 0, 4, 16);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (11, 1, 4, 75);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (12, 2, 4, 15);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (13, 0, 5, 5);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (14, 2, 5, 60);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (15, 0, 6, 100);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (16, 2, 6, 20);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (17, 1, 6, 50);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (18, 0, 7, 16);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (19, 1, 7, 75);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (20, 2, 7, 15);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (21, 0, 8, 20);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (22, 2, 8, 200);

insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (23, 0, 9, 20);
insert into PlaneSeats (id, seatType, plane, availabilityNumber) values (24, 2, 9, 200);

-- Generating data for Flights:
use GammaAir;

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (0, 36, '2022-12-22 07:50:00', '2022-12-22 12:17:00', false, 'A2', 'B34', 0, 4, 5, 0, 2);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (1, 1200, '2022-12-23 21:22:00', '2022-12-23 23:19:00', false, 'C65', 'A43', 9, 4, 2, 9, 4);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (2, 726, '2022-12-23 21:12:00', '2022-12-24 01:36:00', true, 'D32', 'E213', 2, 7, 7, 9, 1);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (3, 383, '2022-12-24 14:24:00', '2022-12-24 20:42:00', true, 'A12', 'A65', 6, 5, 7, 4, 6);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (4, 297, '2022-12-23 19:00:00', '2022-12-24 00:06:00', false, 'B47', 'D12', 5, 3, 8, 3, 5);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (5, 978, '2022-12-25 16:00:00', '2022-12-26 05:43:00', false, 'A23', 'D12', 3, 0, 9, 8, 1);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (6, 398, '2022-12-26 17:44:00', '2022-12-26 19:51:00', false, 'C39', 'A1', 8, 2, 3, 2, 3);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (7, 834, '2022-12-26 00:27:00', '2022-12-27 00:49:00', false, 'G92', 'A34', 1, 2, 4, 5, 3);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (8, 114, '2022-12-27 07:30:00', '2022-12-28 06:34:00', false, 'A2', 'E43', 4, 5, 0, 3, 8);

insert into Flights (id, baseCost, departureTime, arrivalTime, cancelled, arrivalGate, departureGate, fromAirport, toAirport, plane, pilot, coPilot)
values (9, 641, '2022-12-29 18:58:00', '2022-12-30 02:55:00', false, 'C36', 'D14', 4, 7, 2, 9, 6);

-- Generating data for ScheduleRequests:
use GammaAir;

insert into ScheduleRequests (reason, pilot, flight) values ('I can\'t make this flight unfortunately, I\'ve got to visit my family then.', 0, 0);
insert into ScheduleRequests (reason, pilot, flight) values ('I won\'t work with this copilot', 3, 4);
insert into ScheduleRequests (reason, pilot, flight) values ('This is my day off.', 9, 2);

-- Generating mock data for reviews (Customers review flights)
use GammaAir;

insert into Reviews (customer, flight, description, score) values (7586001, 0, 'Extremely stale food, I was starving for the entire 14-hour flight', 2);

insert into Reviews (customer, flight, description, score) values (7586001, 1, 'I thought the flight went smoothly, just wish my leg did not cramp up in the last hour', 4);

insert into Reviews (customer, flight, description, score) values (5928192, 2, 'Cannot imagine this flight having gone better', 5);

insert into Reviews (customer, flight, description, score) values (2943577, 3, 'So much turbulence, I thought I was going to die', 2);

insert into Reviews (customer, flight, description, score) values (5104420, 4, 'The couple sitting next to me had the most annoying kid', 1);

insert into Reviews (customer, flight, description, score) values (3935181, 5, 'Pretty much what I expected out of this flight', 4);

insert into Reviews (customer, flight, description, score) values (6227087, 6, 'The flight went fine, I do wish the flight attendants were more confident of the flying abilities of the pilot though', 3);

insert into Reviews (customer, flight, description, score) values (3696313, 7, 'My positive flight experience made the long journey seem a bit shorter', 4);

insert into Reviews (customer, flight, description, score) values (3232291, 8, 'Best experience of my life', 2);

insert into Reviews (customer, flight, description, score) values (1894155, 9, 'My plane crashed.', 1);

-- Generating mock data for tickets (Customers purchase tickets for flights)
use GammaAir;

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (6213070, 7586001, 0, 0, 'none', true, false, 108);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (1959297, 6567114, 1, 0, 'N/A', true, true, 238);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (5582141, 5928192, 1, 0, 'deathly allegric to all nuts', false, false, 129);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (1476642, 2943577, 2, 1, 'none', true, false, 50);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (0925452, 5104420, 6, 2, 'none', true, false, 146);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (8710188, 3935181, 7, 1, 'N/A', false, false, 535);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (5931780, 6227087, 9, 0, 'will throw up if I smell cheese', true, false, 202);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (3659442, 3696313, 8, 0, 'none', true, true, 212);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (0111098, 3696313, 8, 0, 'none', false, false, 133);

insert into Tickets (id, customer, flight, seatType, accommodations, insuredTrip, hasDisability, checkedBaggageWeight)
values (8873675, 1894155, 2, 2, 'N/A', true, false, 87);

-- Create mock Questions data (Customers ask questions to CustomerReps)
use GammaAir;

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (1945218, 'What is the maximum baggage weight I can check in with my airline before getting charged extra?',
        '100 pounds', true, 7586001, 1330501, 0, 0, 1465692);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (1234567, 'What is my Airline?', 'Jet Blue', true, 6567114, 0087498, 1, 9, 1013398);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (8901234, 'When does my Flight take off?', '11:00 AM EST but boarding starts at 10:00 AM EST', true,
        2943577, 2346794, 2, 9, 1013398);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (5678901, 'Can you confirm that I purchased two tickets?',
        'Yes, you have two tickets purchased.',
        true, 3696313, 1330501, 8, 3, 1465692);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (2345678, 'Are the pilot and co-pilot best friends', 'of course', true,
        5104420, 2346794, 6, 2, 2118212);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (9012345, 'Why are your flights so unpredictable?', null, false,
        3935181, 0087498, 7, 5, 2118212);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (6789012, 'What is the chance my flight will be delayed?', 'Your guess is as good as mine',
        true, 5928192, 2346794, 1, 9, 1013398);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (3456789, 'When does the sun go down tonight?', 'This feels like a question for the weather app',
        true, 5928192, 2346794, 1, 9, 1013398);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (1011213, 'What is my favorite color?', 'I do not get paid enough to answer that',
        true, 5928192, 2346794, 1, 9, 1013398);

insert into Questions (id, question, response, isResolved, customer, customerRep, flight, pilot, airline)
values (1317438, 'Who is the current President?', 'Are you dumb?', true,
        5928192, 2346794, 1, 9, 1013398);