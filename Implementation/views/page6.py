import streamlit as st
import pandas as pd
import os

# File path for storing office locations
OFFICE_CSV_FILE = "Utilities/office_locations.csv"

# Function to load office locations from CSV
def load_office_locations():
    if os.path.exists(OFFICE_CSV_FILE):
        df = pd.read_csv(OFFICE_CSV_FILE)
        return df["Office Location"].tolist()  # Return as a list of locations
    return []

# Function to save a new office location
def save_office_location(office_location):
    df = pd.DataFrame({"Office Location": [office_location]})  # Create DataFrame
    if os.path.exists(OFFICE_CSV_FILE):
        df_existing = pd.read_csv(OFFICE_CSV_FILE)
        df = pd.concat([df_existing, df], ignore_index=True)  # Append new location
    df.to_csv(OFFICE_CSV_FILE, index=False)  # Save to CSV

# Streamlit UI
st.title("Add Office Locations")

with st.form("office_form"):
    st.subheader("Add a New Office Location")
    office_location = st.text_input("Office Location")
    submit_button = st.form_submit_button("Add Location")

    if submit_button:
        if office_location:
            save_office_location(office_location)
            st.success(f"Office location '{office_location}' added successfully!")
        else:
            st.error("Please enter an office location.")

# Display added office locations
office_locations = load_office_locations()
if office_locations:
    st.subheader("Existing Office Locations")
    st.table(pd.DataFrame({"Office Locations": office_locations}))
