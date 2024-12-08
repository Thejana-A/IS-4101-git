# This has the code, after adjusting code to organoze meetings, eliminating unauthorized participants in agenda.
# This adjustment was made on Dec 07.

import time # For calculating time spent for execution

# Start - data set
# Mapping locations, considering that onsite, remote_private are always private
location_map = {"onsite": 1, "remote_private": 2, "remote_public": 3}
# Mapping participants to their groups
participant_groups = {
    'a': {1, 2, 3},
    'b': {4, 5},
    'c': {1, 5, 6, 7, 8}
}
# Availabile time slots and locations of participants
availability_dictionary = [
    {"person": 1, "slot": 1, "location": 1},
    {"person": 1, "slot": 2, "location": 1},
    {"person": 1, "slot": 3, "location": 1},
    {"person": 2, "slot": 2, "location": 2},
    {"person": 2, "slot": 3, "location": 1},
    {"person": 3, "slot": 2, "location": 3},
    {"person": 3, "slot": 3, "location": 1},
    {"person": 3, "slot": 4, "location": 2},
    {"person": 4, "slot": 1, "location": 1},
    {"person": 4, "slot": 2, "location": 1},
    {"person": 4, "slot": 3, "location": 1},
    {"person": 4, "slot": 4, "location": 1},
    {"person": 4, "slot": 4, "location": 3},
    {"person": 5, "slot": 2, "location": 2},
    {"person": 5, "slot": 3, "location": 1},
    {"person": 5, "slot": 4, "location": 2},
    {"person": 6, "slot": 2, "location": 1},
    {"person": 6, "slot": 3, "location": 1}
]
# End - data set

# Resolver function to convert participant groups into individual participants
def document_acl_group_resolver(documents_acl_with_groups): # Pass the document with groups in ACL as a parameter
    resolved_participants = set()
    for item in documents_acl_with_groups:
        if isinstance(item, int):  # If it's a participant ID, add it to the set
            resolved_participants.add(item)
        elif isinstance(item, str):  # If it's a group name, add its participants
            group_participants = participant_groups.get(item, set())
            resolved_participants.update(group_participants)
    return resolved_participants


def participant_validation(documents_acl, agenda_acl):
    if not documents_acl:
        return set(), 0, set(), 0, "", set(), set()  # Return default values if no ACLs are provided
    
    participants_not_in_intersection = set() # Set for participants not in the intersection
    doc_except_agenda_intersection = set() # Set for valid participants for meeting
    contains_public = [0 in doc for doc in documents_acl]  # Check if "public" role (0) is in each document's ACL
    print(contains_public)

    # Step 1: Resolve ACLs of documents except the agenda
    if all(contains_public):  # If all documents contain "public"
        print("All docs are public.")
        doc_except_agenda_intersection.add(0)  # Include "public" as a valid participant
        number_of_documents = len(documents_acl)
    elif not any(contains_public):  # If no document contains "public"
        print("All docs are private.")
        intersection = set.intersection(*documents_acl)  # Calculate intersection of all sets
        doc_except_agenda_intersection = intersection
        number_of_documents = len(documents_acl)
        # Find participants not in intersection
        for s in documents_acl:
            for elem in s:
                if elem not in intersection:
                    participants_not_in_intersection.add(-elem)  # Negative of elem for unauthorized participants
    else:  # Mixed private and public docs
        print("Private and public docs both.")
        private_documents = [s for s in documents_acl if 0 not in s]  # Filter for private docs
        intersection = set.intersection(*private_documents)  # Calculate intersection of private docs
        doc_except_agenda_intersection = intersection
        number_of_documents = len(documents_acl)
        # Find participants not in intersection
        for s in documents_acl:
            for elem in s:
                if elem not in intersection:
                    participants_not_in_intersection.add(-elem)  # Negative of elem for unauthorized participants
    
    total_number_of_docs = number_of_documents + 1  # Count total documents, including agenda

    # Step 2: Resolve ACL for agenda and other docs
    agenda_doc_acl = agenda_acl  # Agenda ACL
    invalid_participants_in_agenda = set()  # Set for invalid participants in agenda
    meeting_type = ""

    if ((0 in doc_except_agenda_intersection) and (0 in agenda_doc_acl)):  # If both docs and agenda are public
        agenda_and_doc_intersection = agenda_doc_acl  # All participants in the agenda including "public"
    elif ((0 in doc_except_agenda_intersection) and (0 not in agenda_doc_acl)):  # If docs are public and agenda is private
        agenda_and_doc_intersection = agenda_doc_acl  # All participants in the agenda, when agenda is not public
    else:  # If private docs and agenda are both private
        agenda_and_doc_intersection = doc_except_agenda_intersection.intersection(agenda_doc_acl)
        invalid_participants_in_agenda = agenda_doc_acl.difference(doc_except_agenda_intersection)  # Invalid participants
    if(len(agenda_and_doc_intersection) > 1):
        meeting_possibility_by_doc_analysis = True
    else:
        meeting_possibility_by_doc_analysis = False

    return total_number_of_docs, participants_not_in_intersection, \
           doc_except_agenda_intersection, agenda_doc_acl, agenda_and_doc_intersection, \
           invalid_participants_in_agenda, meeting_possibility_by_doc_analysis


def time_slot_selection(availability_dictionary, agenda_and_doc_intersection, meeting_quorum):
    # Determine meeting type (public or private)
    if (len(agenda_and_doc_intersection) < 2):
        meeting_type = "invalid meeting"  
    elif (0 in agenda_and_doc_intersection):
        index_for_participant_1 = 1
        meeting_type = "public meeting"       
    else:
        index_for_participant_1 = 0
        meeting_type = "private meeting"
    print("meeting type: ", meeting_type)
    
    # Step 1: Find available time slots for participants
    agenda_and_doc_intersection = list(agenda_and_doc_intersection)
      
    # Create a dictionary to store available participants for each time slot
    slot_participants = {}

    # Iterate over the availability dictionary
    for entry in availability_dictionary:
        person = entry["person"]
        slot = entry["slot"]
        location = entry["location"]
        
        # Only consider participants who are in agenda_and_doc_intersection
        if ((person in agenda_and_doc_intersection) and ((meeting_type == "private meeting" and location != 3) or (meeting_type == "public meeting"))):
            # If the slot is not in the dictionary, initialize it
            if slot not in slot_participants:
                slot_participants[slot] = {}
            
            # Add the person to the set of available participants for the slot
            if person not in slot_participants[slot]:
                slot_participants[slot][person] = location
    
    # Filter the slots where the number of available participants meets the quorum
    valid_time_slots = []
    for slot, participants in slot_participants.items():
        if len(participants) >= meeting_quorum:
            valid_time_slots.append({
                "slot": slot,
                "participants": participants
            })

    if valid_time_slots:
        print("Availability of a quorum satisfying time slot: True")
    else:
        print("Availability of a quorum satisfying time slot: False")
    
    return valid_time_slots



# This function is to select the meeting mode
def meeting_mode_solver(earliest_time_slot):
    earliest_time_slot = earliest_time_slot # Create a local dictionaty variable to assign values passed as parameter
    meeting_mode = ""

    are_all_values_one = all(value == 1 for value in earliest_time_slot['participants'].values()) # Check if all values are 1
    count_ones = sum(1 for value in earliest_time_slot['participants'].values() if value == 1)
    at_least_two_values_are_one = (count_ones >= 2) # Check if there are at least 2 values that are 1

    if are_all_values_one:
        meeting_mode = "onsite"
    elif at_least_two_values_are_one:
        meeting_mode = "hybrid"
    else:
        meeting_mode = "online"
    
    return meeting_mode, earliest_time_slot


def execute_meeting_organizer():
    # Example usage 1 : document_except_agenda_solver(doc_without_agenda) for docuemnts without agenda
    doc1 = {'a', 'b', 10, 11}
    doc2 = {0}
    doc3 = {2, 3, 4, 5, 9, 10, 11}
    doc4 = {2, 3, 4, 5, 6} 
    doc_without_agenda = [document_acl_group_resolver(doc1), doc2, doc3, doc4]
    agenda = {0, 3, 4, 9, 10}
    meeting_quorum = 2
    total_number_of_docs, participants_not_in_intersection, doc_except_agenda_intersection, agenda_doc_acl, agenda_and_doc_intersection, invalid_participants_in_agenda, meeting_possibility_by_doc_analysis = participant_validation(doc_without_agenda, agenda)
    print("(INPUT) doc_without_agenda: ", doc_without_agenda)
    print("(INPUT) agenda: ", agenda)
    print("total_number_of_docs: ", total_number_of_docs)
    print("participants_not_in_intersection: ", participants_not_in_intersection)
    print("doc_except_agenda_intersection: ", doc_except_agenda_intersection)
    print("agenda_doc_acl: ", agenda_doc_acl)
    print("agenda_and_doc_intersection: ", agenda_and_doc_intersection)
    print("invalid_participants_in_agenda: ", invalid_participants_in_agenda)
    print("meeting_possibility_by_doc_analysis(At least 2 participants): ", meeting_possibility_by_doc_analysis)
    print("")

    valid_time_slots = time_slot_selection(availability_dictionary, agenda_and_doc_intersection, meeting_quorum)
    print("valid_time_slots: ", valid_time_slots)
    print("")

    if (len(valid_time_slots) > 0):
        meeting_mode, earliest_time_slot = meeting_mode_solver(valid_time_slots[0])
        print("earliest_time_slot: ", earliest_time_slot)
        print("meeting_mode: ", meeting_mode)
    else:
        print("No eligible time slot !!")

# Execute above workflow while calculating the time spent
start_time = time.time()  # Record start time
execute_meeting_organizer() # Call above major function including the workflow
end_time = time.time()  # Record end time
elapsed_time = end_time - start_time  # Calculate elapsed time
print(f"Time spent: {elapsed_time:.8f} seconds")
