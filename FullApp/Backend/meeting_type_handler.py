def determine_meeting_type(file_permissions):
    """
    Determines whether the meeting is public or private based on file descriptions.

    Args:
        file_permissions (list): A list of dictionaries containing file details.
                                 Each dictionary should include a 'Description' key.

    Returns:
        str: "Public Meeting" if all files have "Public" in their description,
             "Private Meeting" otherwise.
    """
    if not file_permissions or not isinstance(file_permissions, list):
        raise ValueError("Invalid file permissions data.")
    
    non_agenda_files = [file for file in file_permissions if "agenda" not in file.get("Document Name", "").lower()]

    # Collect descriptions from file permissions
    descriptions = [
        file.get("Description", "") for file in non_agenda_files if isinstance(file, dict)
    ]

    # Check if all descriptions contain "Public"
    is_public_meeting = all("Public" in desc for desc in descriptions)

    return "Public Meeting" if is_public_meeting else "Private Meeting"