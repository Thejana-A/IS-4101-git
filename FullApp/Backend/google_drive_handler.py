import re
from Utilities.api import Create_Service
import streamlit as st
import json
import pandas as pd

CLIENT_SECRET_FILE = 'Utilities/client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

def validate_google_folder_link(link: str) -> bool:
    google_folder_pattern = r"https://drive\.google\.com/drive/folders/([\w-]+)"
    # google_folder_pattern = r"https://drive\.google\.com/drive/u/0/folders/([\w-]+)"
    return re.match(google_folder_pattern, link) is not None

def extract_folder_id(link: str) -> str:
    folder_id = link.split("/")[-1]
    return folder_id

def authenticate_google_drive_api():
    try:
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        return service
    except Exception as e:
        raise RuntimeError(f"Failed to authenticate with Google Drive API: {e}")
    
#This is if we are using json file
#def load_group_members(file_path="group_members.json"):
#    try:
#        with open(file_path, "r") as file:
#            group_mapping = json.load(file)
#        return group_mapping
#    except Exception as e:
#        raise RuntimeError(f"Failed to load group members file: {e}")

#For csv file
def load_group_members(csv_path):
    try:
        # Load the CSV file
        df = pd.read_csv(csv_path)

        # Convert CSV data to a dictionary {group_email: [member1, member2, ...]}
        group_mapping = {
            row["Group Email"]: row["Members"].split(", ")
            for _, row in df.iterrows()
        }

        return group_mapping
    except Exception as e:
        raise RuntimeError(f"Failed to load group members file: {e}")

def list_files_in_folder_with_permissions(folder_id: str):
    #group_file = "Utilities/group_members.json"
    group_file = "Utilities/groups_data.csv"

    try:
        # Load group members mapping
        group_mapping = load_group_members(group_file)

        # Authenticate with the API
        service = authenticate_google_drive_api()

        # Query to get all files in the folder
        results = service.files().list(
            q=f"'{folder_id}' in parents",
            fields="files(id, name, description)",
        ).execute()

        files = results.get("files", [])
        all_files_permissions = []
        #file_permissions = []
        table_data = []

        for file in files:
            file_id = file["id"]
            file_name = file["name"]
            file_description = file.get("description", "-")
            
            permissions = service.permissions().list(
                fileId=file_id,
                fields="permissions(emailAddress)",
            ).execute()

            # Process permissions
            permissioned_emails = set()  # Using set to avoid duplicates

            for perm in permissions.get("permissions", []):
                email = perm.get("emailAddress", "N/A")
                if email in group_mapping:
                    # Add group email and its members
                    #permissioned_emails.add(f"**{email}**")  # Add the group email with bold formatting
                    for member in group_mapping[email]:
                        permissioned_emails.add(member)  # Add the member emails (no bold)
                else:
                    permissioned_emails.add(email)

            all_files_permissions.append({
                "Document Name": file_name,
                "Description": file_description,
                "Permissioned Emails": list(permissioned_emails)
            })
    
        return all_files_permissions
    except Exception as e:
        raise RuntimeError(f"Failed to list files in the folder: {e}")

def process_folder_link(link: str):
    # Validate the link
    if not validate_google_folder_link(link):
        return False, "Invalid Google Drive folder link."

    # Extract folder ID
    folder_id = extract_folder_id(link)

    try:
        # Fetch files and permissions
        files_with_permissions = list_files_in_folder_with_permissions(folder_id)
        if files_with_permissions:
            return files_with_permissions
        else:
            return ""
    except RuntimeError as e:
        return False, str(e)