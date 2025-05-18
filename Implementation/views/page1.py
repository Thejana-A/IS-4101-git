import streamlit as st
import pdfplumber
import docx2txt
from Backend.google_drive_handler import process_folder_link
from Backend.email_intersection import get_intersection_of_permissioned_emails, get_agenda_document
from Backend.meeting_type_handler import determine_meeting_type
from Backend.allowed_participants_handler import get_allowed_participants

st.title("Meeting Sheduling Buddy")
st.subheader("Hi, Poornima")

## Save the folder link in session state
if "folder_link" not in st.session_state:
    st.session_state.folder_link = ""
    
# Input box for the Google Drive folder link
folder_link = st.text_input("Enter Google Drive Folder Link", value=st.session_state.folder_link)
#st.session_state.folder_link = folder_link

if st.button("Submit"):
    st.session_state.folder_link = folder_link

# Process the folder link when the user presses the button
if st.session_state.folder_link:
    if folder_link:
        # Call backend function to process the folder link
        file_permissions = process_folder_link(folder_link)

        # Prepare data for Streamlit table
        table_data = []
        for file in file_permissions:
            table_data.append({
                "Document Name": file["Document Name"],
                "Description": file["Description"],
                "Permissioned Emails": ", ".join(file["Permissioned Emails"]),  # Newline-separated emails
            })

        ## Display file details as a table
        st.subheader("File Details")
        st.markdown(
            """
            <style>
            .streamlit-table {
                max-width: 65rem;  /* Limits the width to 65rem, but can stretch */
                width: 100%;  /* Stretches to fill the container up to 65rem */
                margin: auto;  /* Centers the table */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.table(table_data)

        # Calculate and display the intersection of permissioned emails
        intersected_emails = get_intersection_of_permissioned_emails(file_permissions)
        st.session_state.intersected_emails = intersected_emails

        st.subheader("Intersected Permissioned Emails - except Agenda")
        if intersected_emails:
            st.table(list(intersected_emails))
            st.session_state['intersected_emails'] = list(intersected_emails)
        else:
            st.write("No intersected emails found.")

        
        agenda_emails, meeting_type = get_agenda_document(file_permissions)
        st.subheader("Agenda Permissioned Emails")
        if agenda_emails:
            st.table(list(agenda_emails))
            st.session_state['agenda_emails'] = list(agenda_emails)
        else:
            st.write("No agenda emails found.")

        st.subheader("Meeting Type")
        if meeting_type:
            if meeting_type == "Public":
                st.success("This is a **Public Meeting**.")
                st.session_state.meeting_type = "Public Meeting"
            else:
                st.warning("This is a **Private Meeting**.")
                st.session_state.meeting_type = "Private Meeting"
        else: 
            st.warning("This is a **Private Meeting**.")
            st.session_state.meeting_type = "Private Meeting"


        #To determine the Public/Pvt for other documets except agenda 
        meeting_type_for_non_agenda = determine_meeting_type(file_permissions)
        st.session_state.meeting_type = meeting_type

        st.subheader("Allowed Participants for the meeting")
        allowed_participants, message = get_allowed_participants(agenda_emails, intersected_emails, meeting_type, meeting_type_for_non_agenda)
        
        # Store in session_state
        st.session_state.allowed_participants = allowed_participants

        st.table(list(allowed_participants))
        st.write(message)

        if len(allowed_participants) < 2:
            st.error("This meeting cannot be held because minimum of 2 for a meeting is not satisfied")
        else:
            if allowed_participants:
                if st.button("Proceed with meeting scheduling ?"):
                    st.switch_page("views/page7.py")
    else:
        st.warning("Please enter a valid Google Drive folder link.")

            