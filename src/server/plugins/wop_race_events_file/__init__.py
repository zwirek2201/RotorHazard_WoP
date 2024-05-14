from eventmanager import Evt
import datetime
import csv

class WOPRaceEventsFile:
    def __init__(self, rhapi):
        self.rhapi = rhapi

    def race_event(self, event):
        heat = self.rhapi.db.heat_by_id(event["heat_id"])
        # Save current date and time
        current_time = datetime.datetime.now()

        # Save heat in CSV file
        filename = "race-events-" + current_time.strftime("%Y-%m-%d.csv")
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time.date(), current_time.time(), heat.display_name, event["_eventName"]])

def initialize(rhapi):
    es = WOPRaceEventsFile(rhapi)
    rhapi.events.on(Evt.RACE_STAGE, es.race_event)
    rhapi.events.on(Evt.RACE_START, es.race_event)
    rhapi.events.on(Evt.RACE_FINISH, es.race_event)
    rhapi.events.on(Evt.RACE_STOP, es.race_event)