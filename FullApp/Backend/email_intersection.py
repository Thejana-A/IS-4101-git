from typing import List, Set, Dict

def get_intersection_of_permissioned_emails(file_permissions: List[Dict[str, List[str]]]) -> Set[str]:
    """
    Get the intersection of permissioned emails across all files.

    Args:
        file_permissions (List[Dict[str, List[str]]]): List of files with their permissioned emails.

    Returns:
        Set[str]: Intersection of permissioned emails across all files.
    """
    if not file_permissions:
        return set()
    
    # Separate Agenda document from the rest
    non_agenda_files = [file for file in file_permissions if "agenda" not in file.get("Document Name", "").lower()]

    # Extract the list of permissioned emails for each file
    all_permissioned_emails = [
        set(email.lower() for email in file["Permissioned Emails"]) for file in non_agenda_files
    ]

    # Get the intersection of all permissioned emails
    intersected_emails = all_permissioned_emails[0]
    for emails in all_permissioned_emails[1:]:
        intersected_emails &= emails  # Perform set intersection

    return intersected_emails


def get_agenda_document(file_permissions: List[Dict[str, List[str]]]) -> Set[str]:
    if not file_permissions:
        return set()
    
    agenda_file = next((file for file in file_permissions if "agenda" in file.get("Document Name", "").lower()), None)
    
    #return set(agenda_file["Permissioned Emails"]) if agenda_file else set()
    if agenda_file:
        return set(agenda_file["Permissioned Emails"]), agenda_file.get("Description", "-")
    
   
