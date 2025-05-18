import streamlit as st
from Utilities.api import Create_Service
from Backend.location_lable import get_location_label

from datetime import datetime
import pytz

CLIENT_SECRET_FILE = 'Utilities/client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar_api():
    try:
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        return service
    except Exception as e:
        raise RuntimeError(f"Failed to authenticate with Google Drive API: {e}")

def parse_working_location(event):
    """
    Parse the workingLocationProperties from an event.
    Args:
        event (dict): A Google Calendar event object.
    Returns:
        str: A string description of the working location.
    """
    if event.get("eventType") != "workingLocation":
        raise ValueError(f"'{event.get('summary', 'Unknown Event')}' is not a working location event.")

    working_location = event.get("workingLocationProperties", {})
    location = "No Location"
    if working_location:
        if working_location.get("type") == "homeOffice":
            location = "Home"
        elif working_location.get("type") == "officeLocation":
            location = working_location.get("officeLocation", {}).get("label", "Office Location")
        elif working_location.get("type") == "customLocation":
            location = working_location.get("customLocation", {}).get("label", "Custom Location")

    return f"{event.get('start', {}).get('date')}: {location}"


def format_event_date_time(start, end):
    try:
        # Convert start and end to datetime objects
        start_dt = datetime.fromisoformat(start) if start else None
        end_dt = datetime.fromisoformat(end) if end else None

        # Format date and time separately
        if start_dt and end_dt:
            formatted_date = start_dt.strftime("%Y-%m-%d")  # 2025-01-23
            start_time = start_dt.strftime("%I:%M %p").lstrip("0")  # 9:00 AM
            end_time = end_dt.strftime("%I:%M %p").lstrip("0")  # 10:00 AM
            formatted_time_slot = f"{start_time} – {end_time}"

            return formatted_date, formatted_time_slot
        return "No Date", "No Time Slot"
    except ValueError:
        return "Invalid Date", "Invalid Time Slot"

def get_events_in_date_range(start_date: str, end_date: str):
    # Check if intersected_emails are in session state
    #using emails coz email = calander_id
    #if 'intersected_emails' in st.session_state:
    #    intersected_emails = st.session_state['intersected_emails']
    #else:
    #    raise ValueError("No intersected emails found in session state.")
    
    if 'allowed_participants' in st.session_state:
        allowed_emails = st.session_state['allowed_participants']
    else:
        raise ValueError("No intersected emails found in session state.")
    
    # Authenticate once
    service = authenticate_google_calendar_api()
    all_filtered_events = []

    # Loop through each email and get events
    for email in allowed_emails:
        try:
            events_result = service.events().list(
                calendarId=email,
                timeMin=start_date,
                timeMax=end_date,
                singleEvents=True,
                orderBy="startTime"
            ).execute()

            events = events_result.get("items", [])

            # Extract and filter events
            filtered_events = [
                {
                    "User Email": email,
                    "Name": event.get("summary", "No Title"),
                    "Location": event.get("location", "No Description"),
                    "Location Label": get_location_label(email, event.get("location", "No Location")),
                    "Date": format_event_date_time(
                        event.get("start", {}).get("dateTime"), 
                        event.get("end", {}).get("dateTime")
                    )[0],
                    "Time Slot": format_event_date_time(
                        event.get("start", {}).get("dateTime"), 
                        event.get("end", {}).get("dateTime")
                    )[1]
                }
                for event in events
            ]

            all_filtered_events.extend(filtered_events)
        
        except Exception as e:
            print(f"Failed to fetch events for {email}: {e}")

    return all_filtered_events

        


#get_events_in_date_range -> filtered_events
#working_locations = []
            
#for event in events:
#    try:
#        location = parse_working_location(event)
#        working_locations.append(location)
#    except ValueError as e:
#        print(e)

#return working_locations