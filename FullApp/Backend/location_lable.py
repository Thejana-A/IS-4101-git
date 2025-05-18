#import json
#import streamlit as st

#defined_location_file = "Utilities/defined_locations.json"

## Load the JSON file
#with open(defined_location_file, "r") as file:
#    predefined_locations = json.load(file)

#def get_location_label(location: str) -> str:
#    if not location:
#        return "No Location"
#    # Check if the location is Work or Home (case insensitive)
#    for label, addresses in predefined_locations.items():
#        if any(address.lower() in location.lower() for address in addresses):
#            return label
#    # If no match, return as Remote Public
#    return "Remote Public"




import streamlit as st
import pandas as pd
import os

# Path to the CSV file
CSV_FILE = "Utilities/users_data.csv"
# File path for storing office locations
OFFICE_CSV_FILE = "Utilities/office_locations.csv"

# Load user home locations from CSV
def load_user_home_locations(csv_path=CSV_FILE):
    try:
        df = pd.read_csv(csv_path)
        return dict(zip(df["Email"], df["Home Location"]))  # {email: home_location}
    except Exception as e:
        raise RuntimeError(f"Error loading user data: {e}")

def load_office_locations():
    if os.path.exists(OFFICE_CSV_FILE):
        df = pd.read_csv(OFFICE_CSV_FILE)
        return df["Office Location"].tolist()  # Return as a list
    return []

def get_location_label(user_email: str, event_location: str) -> str:
    if not event_location:
        return "No Location"

    # Load user home locations
    user_home_locations = load_user_home_locations()

    # Check if event location matches user's home location
    if user_email in user_home_locations and event_location.lower() == user_home_locations[user_email].lower():
        return "Home"

    # Load office locations from CSV
    office_locations = load_office_locations()
    if any(office.lower() in event_location.lower() for office in office_locations):
        return "Work"

    # Default to Remote Public
    return "Remote Public"



