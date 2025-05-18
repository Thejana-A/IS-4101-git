import streamlit as st
import pandas as pd
import os

# Path to the CSV file
CSV_FILE = "Utilities/users_data.csv"

# Function to load existing data from CSV
def load_users_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        # If the file doesn't exist, create it with the correct columns
        return pd.DataFrame(columns=["Name", "Email", "Home Location", "Calendar ID"])

# Function to save new user data to CSV
def save_user_to_csv(user_data):
    df = load_users_data()
    
    # Convert the user_data dictionary into a DataFrame to concatenate
    new_user_df = pd.DataFrame([user_data])
    
    # Concatenate the new user data to the existing dataframe
    df = pd.concat([df, new_user_df], ignore_index=True)
    
    # Save the updated DataFrame back to CSV
    df.to_csv(CSV_FILE, index=False)

# Initialize session state
if "users_data" not in st.session_state:
    st.session_state.users_data = load_users_data()

# Function to handle form submission
def add_user(name, email, home_location, calendar_id):
    user_data = {
        "Name": name,
        "Email": email,
        "Home Location": home_location,
        "Calendar ID": calendar_id
    }
    save_user_to_csv(user_data)
    st.session_state.users_data = load_users_data()  # Reload the updated list
    st.success(f"User {name} added successfully!")

# Display title
st.title("Admin Panel - Add User")

# User Input Form
with st.form(key="user_form"):
    st.subheader("Add New User")

    name = st.text_input("Name")
    email = st.text_input("Email")
    home_location = st.text_input("Home Location")
    calendar_id = st.text_input("Calendar ID")

    submit_button = st.form_submit_button("Add User")

    if submit_button:
        if name and email and home_location and calendar_id:
            add_user(name, email, home_location, calendar_id)
        else:
            st.error("Please fill in all fields!")

# Display added users in a table
if not st.session_state.users_data.empty:
    st.subheader("Users List")
    st.table(st.session_state.users_data)



#import streamlit as st
#import pandas as pd
#import os
#import re
#from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode

## Path to the CSV file
#CSV_FILE = "Utilities/users_data.csv"

## Load existing data
#def load_users_data():
#    if os.path.exists(CSV_FILE):
#        return pd.read_csv(CSV_FILE)
#    else:
#        return pd.DataFrame(columns=["Name", "Email", "Home Location", "Calendar ID"])

## Save entire DataFrame to CSV
#def save_users_data(df):
#    df.to_csv(CSV_FILE, index=False)

## Save new user to CSV
#def save_user_to_csv(user_data):
#    df = load_users_data()
#    new_user_df = pd.DataFrame([user_data])
#    df = pd.concat([df, new_user_df], ignore_index=True)
#    save_users_data(df)

## Delete user by index
#def delete_user(index):
#    df = load_users_data()
#    df = df.drop(index).reset_index(drop=True)
#    save_users_data(df)
#    st.session_state.users_data = df

## Update user by index
#def update_user(index, user_data):
#    df = load_users_data()
#    for key in user_data:
#        df.at[index, key] = user_data[key]
#    save_users_data(df)
#    st.session_state.users_data = df

## Email format validator
#def is_valid_email(email):
#    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

## Initialize session state
#if "users_data" not in st.session_state:
#    st.session_state.users_data = load_users_data()

#if "edit_index" not in st.session_state:
#    st.session_state.edit_index = None

## Title with Add User Button
#title_col, button_col = st.columns([6, 1])
#with title_col:
#    st.title("Admin Panel - Manage Users")
#with button_col:
#    if st.button("➕ Add User"):
#        st.session_state.edit_index = None
#        st.rerun()

## User form
#with st.form(key="user_form"):
#    st.subheader("Add New User" if st.session_state.edit_index is None else "Edit User")

#    if st.session_state.edit_index is not None:
#        selected_user = st.session_state.users_data.iloc[st.session_state.edit_index]
#        name = st.text_input("Name", value=selected_user["Name"])
#        email = st.text_input("Email", value=selected_user["Email"])
#        home_location = st.text_input("Home Location", value=selected_user["Home Location"])
#        calendar_id = st.text_input("Calendar ID", value=selected_user["Calendar ID"])
#    else:
#        name = st.text_input("Name")
#        email = st.text_input("Email")
#        home_location = st.text_input("Home Location")
#        calendar_id = st.text_input("Calendar ID")

#    submit_button = st.form_submit_button("Update" if st.session_state.edit_index is not None else "Add User")

#    if submit_button:
#        if not (name and email and home_location and calendar_id):
#            st.error("❗ All fields are required!")
#        elif not is_valid_email(email):
#            st.error("❗ Please enter a valid email address.")
#        elif st.session_state.edit_index is None and email in st.session_state.users_data["Email"].values:
#            st.error("❗ Email already exists!")
#        else:
#            user_data = {
#                "Name": name,
#                "Email": email,
#                "Home Location": home_location,
#                "Calendar ID": calendar_id
#            }

#            if st.session_state.edit_index is not None:
#                update_user(st.session_state.edit_index, user_data)
#                st.success(f"✅ User '{name}' updated successfully!")
#                st.session_state.edit_index = None
#            else:
#                save_user_to_csv(user_data)
#                st.success(f"✅ User '{name}' added successfully!")

#            st.session_state.users_data = load_users_data()
#            st.rerun()

## Display users
#if not st.session_state.users_data.empty:
#    st.subheader("Current Users")

#    for i, row in st.session_state.users_data.iterrows():
#        cols = st.columns([2, 3, 2, 3, 1, 1])
#        cols[0].markdown(f"**{row['Name']}**")
#        cols[1].markdown(f"{row['Email']}")
#        cols[2].markdown(f"{row['Home Location']}")
#        cols[3].markdown(f"{row['Calendar ID']}")
#        if cols[4].button("✏️", key=f"edit_{i}"):
#            st.session_state.edit_index = i
#            st.rerun()
#        if cols[5].button("🗑️", key=f"delete_{i}"):
#            delete_user(i)
#            st.success(f"🗑️ User '{row['Name']}' deleted.")
#            st.rerun()

#        # Add horizontal line after each row
#        st.markdown('<hr style="margin-top: 4px; margin-bottom: 4px; border: 0.5px solid #ccc;" />', unsafe_allow_html=True)
#else:
#    st.info("No users added yet.")


#st.table(st.session_state.users_data)





