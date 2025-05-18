import streamlit as st
import pandas as pd
import os

# Path to the CSV file for groups
GROUP_CSV_FILE = "Utilities/groups_data.csv"

# Function to load existing groups from CSV
def load_groups_data():
    if os.path.exists(GROUP_CSV_FILE):
        return pd.read_csv(GROUP_CSV_FILE)
    else:
        return pd.DataFrame(columns=["Group Email", "Members"])

# Function to save new group data to CSV
def save_group_to_csv(group_email, member_emails):
    df = load_groups_data()
    
    # Join member emails into a single string
    members_str = ", ".join(member_emails)
    
    # Create a new group DataFrame
    new_group_df = pd.DataFrame([{"Group Email": group_email, "Members": members_str}])
    
    # Concatenate the new group data to the existing dataframe
    df = pd.concat([df, new_group_df], ignore_index=True)
    
    # Save the updated DataFrame back to CSV
    df.to_csv(GROUP_CSV_FILE, index=False)

# Initialize session state for groups
if "groups_data" not in st.session_state:
    st.session_state.groups_data = load_groups_data()

# Function to handle group form submission
def add_group(group_email, member_emails):
    valid_members = [email for email in member_emails if email]  # Remove empty fields

    if group_email and valid_members:
        save_group_to_csv(group_email, valid_members)
        st.session_state.groups_data = load_groups_data()
        st.success(f"Group {group_email} added successfully!")
    else:
        st.error("Please provide a group email and at least one member!")

# Display title
st.title("Admin Panel - Add Group")

# --- Group Input Form ---
with st.form(key="group_form"):
    st.subheader("Add New Group")

    group_email = st.text_input("Group Email")

    # Allow up to 5 members
    member_emails = [
        st.text_input("Member Email 1"),
        st.text_input("Member Email 2"),
        st.text_input("Member Email 3"),
        st.text_input("Member Email 4"),
        st.text_input("Member Email 5"),
    ]

    submit_group = st.form_submit_button("Add Group")

    if submit_group:
        add_group(group_email, member_emails)

# Display Groups Table
if not st.session_state.groups_data.empty:
    st.subheader("Groups List")
    
    # Only show Group Email and a single Members column
    display_df = st.session_state.groups_data[["Group Email", "Members"]]
    st.table(display_df)
