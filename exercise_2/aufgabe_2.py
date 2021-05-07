# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:03:00 2020

@author: David
"""

import pandas as pd

airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")
flights = pd.read_csv("flights_100.csv")

airlines.dtypes
airports.dtypes
flights.dtypes

"""
1.1 

Fakten:
TAXI_OUT    
WHEELS_OFF    
SCHEDULED_TIME
ELAPSED_TIME
AIR_TIME
DISTANCE
WHEELS_ON
TAXI_IN
ARRIVAL_DELAY
DIVERTED
Details(AIR_SYSTEM_DELAY,SECURITY_DELAY,AIRLINE_DELAY,LATE_AIRCRAFT_DELAY,WEATHER_DELAY)


Dimensionen:
Time(YEAR.MONTH,DAY,DAY_OF_WEEK)
Operator(AIRLINE (FLIGHT_NUMBER,TAIL_NUMBER))
Airport_Location(ORIGIN_AIRPORT,DESTINATION_AIRPORT)
Location(AIRPORT,CITY,STATE,COUNTRY)
Details(CANCELLED,CANCELLATION_REASON)
? Other(SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY, SCHEDULED_ARRIVAL, 
        ARRIVAL_TIME)

Dimensionsschema:
SCHEDULED_TIME -> DAY / DAY_OF_WEEK -> MONTH -> YEAR -> TOP
ORIGIN_AIRPORT -> AIRPORT -> CITY -> STATE -> COUNTRY
"""

"""
1.2 

!!LINK TO M/ER DIAGRAMM ON LUCIDCHART!!
https://lucid.app/lucidchart/invitations/accept/2770dee5-17e9-43d3-93cd-48593db2cf2b

"""