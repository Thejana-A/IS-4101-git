# Start - data set
# Mapping locations, considering that onsite is always private, to conduct onsite meetings
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
    {"person": 1, "slot": 2, "location": 2},
    {"person": 1, "slot": 3, "location": 2},
    {"person": 2, "slot": 2, "location": 1},
    {"person": 2, "slot": 3, "location": 2},
    {"person": 3, "slot": 2, "location": 3},
    {"person": 3, "slot": 3, "location": 1},
    {"person": 4, "slot": 1, "location": 1},
    {"person": 5, "slot": 2, "location": 1},
    {"person": 6, "slot": 1, "location": 1},
    {"person": 7, "slot": 2, "location": 3},
    {"person": 7, "slot": 3, "location": 3},
    {"person": 8, "slot": 1, "location": 1},
    {"person": 9, "slot": 1, "location": 1},
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


# Pure maxsat solver : This function is to resolve soft clauses (Each group must satisfy at least one) to find the intersection of ACL of documents except the agenda
def document_maxsat_solver(documents_acl):
    if not documents_acl:
        return set(), 0, set(), 0  # Return empty intersection, count, hard clauses, and satisfiable count if no sets are provided
    
    hard_clauses = set() # Create hard clauses for participants not in the intersection
    valid_participants = set() # Create an empty set to add valid participants for meeting
    contains_public = [0 in doc for doc in documents_acl] # Check whether "public" role (represented by '0') is present in these ACLs
    print(contains_public)
    if all(contains_public): # Check whether all documents contain "public"
        print("All docs are public.")
        valid_participants.add(0) # Include "public" (any person) as the valid participant in meeting
        soft_clauses = len(documents_acl) # Count soft clauses (one for each set)
    elif not any(contains_public):
        print("All docs are private")
        intersection = set.intersection(*documents_acl) # Calculate the intersection of all sets
        valid_participants = intersection # Assign intersection as set of valid participants
        soft_clauses = len(documents_acl) # Count soft clauses (one for each set)
        for s in documents_acl: # Identify the participants not in intersection as derived hard claused
            for elem in s:
                if (elem not in intersection):
                    hard_clauses.add(-elem)  # Just use the element directly, if needed
    else:
        print("Private and public docs both.")
        private_documents = [s for s in documents_acl if 0 not in s] # Filter & get only private documents
        intersection = set.intersection(*private_documents)
        valid_participants = intersection # Assign intersection as set of valid participants
        soft_clauses = len(documents_acl) # Count soft clauses (one for each set)
        for s in documents_acl: # Identify the participants not in intersection as derived hard claused
            for elem in s:
                if (elem not in intersection):
                    hard_clauses.add(-elem)  # Just use the element directly, if needed
    # Total clauses count
    total_clauses = soft_clauses + (1 if hard_clauses else 0)  # Count hard clauses as one if exists
    # Output the result
    return valid_participants, total_clauses, hard_clauses, soft_clauses  # Total clause count


# Partial maxsat solver : This function is to resolve participants of documents ACL as soft clause (Not mandatory participants) and agenda ACL as hard clause (Each memeber except "public" [represented by 0] is mandatorily required)
def agenda_maxsat_solver(documents_acl_participants, agenda_acl):
    soft_clause = documents_acl_participants # Define participants of ACL of other docs as soft clause
    hard_clause = agenda_acl # Define ACL of agenda as hard clause
    invalid_participants_in_agenda = set() # Create a set to include participants in agenda, but absent in ACL of docs
    meeting_status = ""
    if ((0 in soft_clause) and (0 in hard_clause)): # Check whether all docs and agenda are public
        agenda_and_doc_participants = hard_clause # Calculate the union of ACL of other documents and agenda
        meeting_status = "public meeting"
    elif ((0 in soft_clause) and (0 not in hard_clause)): # Check whether all docs are public and agenda is private
        agenda_and_doc_participants = hard_clause
        meeting_status = "private meeting"
    elif ((0 not in soft_clause) and (0 in hard_clause)): # Check whether private docs are present and agenda is public
        agenda_and_doc_participants = hard_clause
        invalid_participants_in_agenda = hard_clause.difference(soft_clause) # Calculate the difference of ACL of ageda and ACL of other documents, to identify if there are invalid (unauthorized) participants in agenda
        meeting_status = "invalid meeting"
    else: # Check whether private docs are present and agenda is also private
        agenda_and_doc_participants = soft_clause.intersection(hard_clause) # Calculate the intersection of ACL of other documents and agenda
        invalid_participants_in_agenda = hard_clause.difference(soft_clause) # Calculate the difference of ACL of ageda and ACL of other documents, to identify if there are invalid (unauthorized) participants in agenda
        if not invalid_participants_in_agenda: # If agenda has no invalid (unauthorized) participants
            meeting_status = "private meeting"
        else: # If agenda has invalid (unauthorized) participants
            meeting_status = "invalid meeting"
    return soft_clause, hard_clause, agenda_and_doc_participants, invalid_participants_in_agenda, meeting_status

# Pure maxsat solver : This function is to find the time slot for meeting by considering available time slots of participants as groups of soft clauses (Each group must satisfy at least one)
def time_slot_maxsat_solver(availability_dictionary, agenda_and_doc_participants):
    availability_dictionary = availability_dictionary # Local dictionary variable for handling the availability dictionary passed as parameter
    agenda_and_doc_participants = list(agenda_and_doc_participants)
    if (0 in agenda_and_doc_participants):
        index_for_participant_1 = 1
    else:
        index_for_participant_1 = 0
    slots_for_participant_1 = {entry["slot"] for entry in availability_dictionary if entry["person"] == agenda_and_doc_participants[index_for_participant_1]}
    time_slot_intersection = slots_for_participant_1
    for i in range((index_for_participant_1+1), len(agenda_and_doc_participants)):
        slots_for_next_participant = {entry["slot"] for entry in availability_dictionary if entry["person"] == agenda_and_doc_participants[i]}
        time_slot_intersection = time_slot_intersection.intersection(slots_for_next_participant)
        if not time_slot_intersection:
            break
    return time_slot_intersection

# This function is to extract the meeting locations of selected meeting slots
def meeting_location_extracter(availability_dictionary, agenda_and_doc_participants, tentative_time_slots):
    availability_dictionary = availability_dictionary # Local dictionary variable for handling the availability dictionary passed as parameter
    agenda_and_doc_participants = list(agenda_and_doc_participants) # Local list variable for handling selected meeting participants passed as parameter
    tentative_time_slots = list(tentative_time_slots) # Local list variable for handling tentative time slots passed as parameter
    meeting_locations = {} # Initialize empty dictionary to store meeting locations

    # Loop through the availability dictionary
    for entry in availability_dictionary:
        person = entry["person"]
        slot = entry["slot"]
        location = entry["location"]
        
        # Check if the person is a selected participant for the meeting
        if ((person in agenda_and_doc_participants) and (slot in tentative_time_slots)):
            if slot not in meeting_locations:
                meeting_locations[slot] = []  # Initialize a list for the slot if not already present
            meeting_locations[slot].append(location)  # Add the location

    return meeting_locations


# Pure maxsat solver : This function is to select the meeting mode
def meeting_mode_maxsat_solver(meeting_locations):
    meeting_locations = meeting_locations # Create a local dictionaty variable to assign values passed as parameter
    optimum_meeting_mode = ""
    optimum_meeting_slot = None

    # Check for "onsite" possibility
    for slot, locations in meeting_locations.items():
        if all(loc == 1 for loc in locations):  # Check if all elements are 1
            optimum_meeting_mode = "onsite"
            optimum_meeting_slot = slot
            break  # Exit the loop since we found an onsite meeting

    if optimum_meeting_mode == "":
        # Check for "hybrid" possibility
        highest_count_ones = 0
        hybrid_slot = None

        for slot, locations in meeting_locations.items():
            count_ones = locations.count(1)
            if count_ones > highest_count_ones:
                highest_count_ones = count_ones
                hybrid_slot = slot

        if highest_count_ones >= 2:  # Check if the highest count of 1s is >= 2
            optimum_meeting_mode = "hybrid"
            optimum_meeting_slot = hybrid_slot

    if optimum_meeting_mode == "":
        # Find the item with the highest number of 2s
        highest_count_twos = 0
        twos_slot = None

        for slot, locations in meeting_locations.items():
            count_twos = locations.count(2)
            if count_twos > highest_count_twos:
                highest_count_twos = count_twos
                twos_slot = slot

        optimum_meeting_mode = "online"  # Set to online since no previous conditions were met
        optimum_meeting_slot = twos_slot  # Assign the slot with the highest number of 2s

    return optimum_meeting_mode, optimum_meeting_slot, meeting_locations[optimum_meeting_slot]


# Example usage 1 : document_maxsat_solver(doc_without_agenda) for docuemnts without agenda
doc1 = {1, 2, 3, 4, 5, 6, 7, 8}
doc2 = {0, 1, 'a', 4, 7, 11, 'c'}
doc2 = document_acl_group_resolver(doc2)
doc_without_agenda = [doc1, doc2]
doc_acl_participants, doc_total_clauses, doc_hard_clauses, doc_soft_clauses = document_maxsat_solver(doc_without_agenda)
print("Participants from documents except agenda:", doc_acl_participants)
print("Maximum satisfiable clauses (excluding hard clause):", doc_soft_clauses)
print("Total number of clauses (including hard clauses):", doc_total_clauses)
print("Soft clauses:", doc_without_agenda)
print("Hard clauses:", doc_hard_clauses)
print("\n")

# Example usage 2 : agenda_maxsat_solver(doc_intersection, agenda) for documents with agenda
agenda = {1, 2, 3, 5, 7}
soft_clause, hard_clause, agenda_and_doc_participants, invalid_participants_in_agenda, meeting_validity = agenda_maxsat_solver(doc_acl_participants, agenda)
print("Soft clause (participants from ACL of docs):", soft_clause)
print("Hard clause (participants from ACL of agenda):", hard_clause)
print("Agenda and other docs participants:", agenda_and_doc_participants)
print("Unauthorized participants in agenda:", invalid_participants_in_agenda)
print("Meeting validity:", meeting_validity)
print("\n")

# Example usage 3 : time_slot_maxsat_solver(availability_dictionary, agenda_and_doc_participants) for finding time slot for meeting
time_slot_intersection = time_slot_maxsat_solver(availability_dictionary, agenda_and_doc_participants)
print("Time slot intersection (Possible time slots for meeting):", time_slot_intersection)
print("\n")

# Example usage 4 : meeting_location_extracter(availability_dictionary, agenda_and_doc_participants, time_slot_intersection) for extracting the meeting locations corresponding to tentative time slots
tentative_meeting_locations = meeting_location_extracter(availability_dictionary, agenda_and_doc_participants, time_slot_intersection)
print("Time slot & Tentative meeting locations for the meeting:", tentative_meeting_locations)
print("\n")

# Example usage 5 : meeting_mode_maxsat_solver(meeting_locations) for selecting the 
optimum_meeting_mode, optimum_meeting_slot, optimum_meeting_locations = meeting_mode_maxsat_solver(tentative_meeting_locations)
print("Optimum meeting mode:", optimum_meeting_mode)
print("Optimum meeting slot:", optimum_meeting_slot)
print("Optimum meeting locations:", optimum_meeting_locations)
print("\n")