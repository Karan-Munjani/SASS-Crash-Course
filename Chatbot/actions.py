# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

covidzones = {
    "Ahmedabad": "Red",
    "Delhi": "Red",
    "Kolkatta": "Green",
    "Banglore": "Orange",
    "Mumbai": "Red",
    "Chennai": "Orange",
    "Thane": "Green",
    "Surat": "Red",
    "Udaipur": "Green",
    "Borivalli": "Orange",
    "North Goa": "Green",
    "Jamnagar": "Orange",
    "Gandhinagar": "Red",
    "Srinagar": "Red"
}

class ActionFindAndShowCovidZone(Action):

    def name(self) -> Text:
        return "action_find_and_show_covid_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")

        covidzone = covidzones.get(city)

        if covidzone is None:
            output = "Could not find the covid zone for {}".format(city)
        else:
            output = "The covid19 zone for {} is {}".format(city, covidzone)

        dispatcher.utter_message(text=output)

        return []
