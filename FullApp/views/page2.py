import streamlit as st
from datetime import datetime, timedelta
from Backend.calendar_handler import get_events_in_date_range
from Backend.meeting_scheduling_handler import filter_permissioned_events, find_earliest_meeting_time

# Ensure the session state variable exists
if "final_meeting_type" not in st.session_state:
    st.error("Add meeting details first.")
else:
    final_meeting_type = st.session_state.final_meeting_type

    if final_meeting_type == "Private":
        if "allowed_participants" in st.session_state:
            allowed = st.session_state.allowed_participants
            st.warning(
                "This is a private meeting with allowed participants with private locations.\n\n"
                + "**Allowed participants are:**\n"
                + ", ".join([f'`{email}`' for email in allowed])
            )
        else:
            st.error("No allowed participants")
        #st.warning("This is a private meeting with allowed participants with private locations. \n\n allowed participants are  ")
    else:
        allowed = st.session_state.allowed_participants
        st.success(
            "This is a public meeting. Anyone can join from any location.\n\n" 
            + "**Filtered participants from document analysis:** " 
            + ", ".join([f'`{email}`' for email in allowed])
        )

quorum = st.session_state.get("quorum_number")
if quorum:
    st.success(f"We have a quorum of **{int(quorum)}** participants.")
else:
    st.warning("We don't have a specific quorum set for this meeting.")

st.title("Schedule a Meeting")

# Initialize session state variables if they don't exist
if "start_date" not in st.session_state:
    st.session_state.start_date = datetime.now().date()
if "end_date" not in st.session_state:
    st.session_state.end_date = (datetime.now() + timedelta(days=7)).date()

# Date Range Picker
st.subheader("Select Date Range")
col1, col2 = st.columns(2)

with col1:
    #start_date = st.date_input("From", value=datetime.now().date())
    start_date = st.date_input("From", value=st.session_state.start_date)
    st.session_state.start_date = start_date  # Update session state
with col2:
    #end_date = st.date_input("To", value=(datetime.now() + timedelta(days=7)).date())
    end_date = st.date_input("To", value=st.session_state.end_date)
    st.session_state.end_date = end_date  # Update session state
    
# Ensure end date is not before start date
if start_date > end_date:
    st.error("End date must be after the start date!")
else:
    # Fetch events on button click
    if st.button("Fetch Events"):
        with st.spinner("Fetching events..."):
            # Convert dates to ISO format
            start_date_iso = datetime.combine(start_date, datetime.min.time()).isoformat() + "Z"
            end_date_iso = datetime.combine(end_date, datetime.max.time()).isoformat() + "Z"

            try:
                events = get_events_in_date_range(start_date_iso, end_date_iso)
                #intersected_emails = st.session_state.intersected_emails
                meeting_type = st.session_state.meeting_type

                new_events = filter_permissioned_events(events, allowed, final_meeting_type)
                #st.write("permissioned", new_events)
                
                if events:
                    # When Displaying only events
                    event_strings = [str(event) for event in events]

                    st.title("All events")
                    st.table(events)

                    st.title("Filtered Events for the Meeting")

                    if not new_events.empty:
                        st.table(new_events)
                        time_slot = find_earliest_meeting_time(new_events, allowed, quorum)
                    else:
                        st.error("No common events to proceed")
                else:
                    st.info("No events found in this date range.")
            except Exception as e:
                st.error(f"Error fetching events: {e}")