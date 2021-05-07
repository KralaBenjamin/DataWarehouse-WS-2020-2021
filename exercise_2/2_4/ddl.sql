
CREATE TABLE [DATE] (
  [NUMBER] <type>,
  [NUMBER] <type>,
  [NUMBER] <type>
);

CREATE INDEX [YEAR] ON  [DATE] ([NUMBER]);

CREATE INDEX [MONTH] ON  [DATE] ([NUMBER]);

CREATE INDEX [DAY] ON  [DATE] ([NUMBER]);

CREATE TABLE [AIRPORT] (
  [IATA_CODE] PRIMARY_KEY,
  [NAME] VARCHAR2,
  [LATTITUDE] FLOAT,
  [LONGITUDE] FLOAT,
  [COUNTRY] VARCHAR2,
  [STATE] VARCHAR2,
  [CITY] VARCHAR2,
  PRIMARY KEY ([IATA_CODE])
);

CREATE TABLE [AIRLINE] (
  [AIRLINE_ID] PRIMARY_KEY,
  [NAME] VARCHAR2,
  [COUNTRY] VARCHAR2,
  [IATA_CODE] PRIMARY_KEY,
  PRIMARY KEY ([AIRLINE_ID])
);

CREATE TABLE [FLIGHT] (
  [FLIGHT_ID] PRIMARY_KEY,
  [TAIL_NUMBER] VARCHAR2,
  [DATE] <type>,
  [AIRLINE_ID] PRIMARY_KEY,
  [FLIGHT_NUMBER] NUMBER,
  [ORIGIN_AIRPORT] PRIMARY_KEY,
  [DESTINATION_AIRPORT] PRIMARY_KEY,
  [DIVERTED] BOOL,
  PRIMARY KEY ([FLIGHT_ID])
);

CREATE INDEX [Key] ON  [FLIGHT] ([DIVERTED]);

CREATE TABLE [DEPARTURE] (
  [FLIGHT_ID] PRIMARY_KEY,
  [SCHEDULED_DEPARTURE] NUMBER,
  [DEPARTURE_TIME] NUMBER,
  [DEPARTURE_DELAY] NUMBER
);

CREATE TABLE [CANCELLATION] (
  [FLIGHT_ID] PRIMARY_KEY,
  [CANCELLED] NUMBER,
  [REASON] CHAR
);

CREATE TABLE [DELAY] (
  [FLIGHT_ID] PRIMARY_KEY,
  [AIR_SYSTEM_DELAY] NUMBER,
  [SECURITY_DELAY] NUMBER,
  [AIRLINE_DELAY] NUMBER,
  [LATE_AIRCRAFT_DELAY] NUMBER,
  [WEATHER_DELAY] NUMBER
);

CREATE TABLE [ARRIVAL] (
  [FLIGHT_ID] PRIMARY_KEY,
  [SCHEDULED_ARRIVAL] NUMBER,
  [ARRIVAL_TIME] NUMBER,
  [ARRIVAL_DELAY] NUMBER
);

