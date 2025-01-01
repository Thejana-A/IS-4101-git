from sympy import symbols  # Correct import for symbols
from sympy.logic.boolalg import Or, And, Not, simplify_logic
from sympy import true, false  # For boolean constants
from itertools import combinations

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
    {"person": "i_1", "slot": "slot1", "location": "onsite"},
    {"person": "i_1", "slot": "slot2", "location": "onsite"},
    {"person": "i_1", "slot": "slot3", "location": "onsite"},
    {"person": "i_2", "slot": "slot2", "location": "remote_private"},
    {"person": "i_2", "slot": "slot3", "location": "onsite"},
    {"person": "i_3", "slot": "slot2", "location": "onsite"},
    {"person": "i_3", "slot": "slot3", "location": "onsite"},
    {"person": "i_4", "slot": "slot1", "location": "onsite"},
    {"person": "i_4", "slot": "slot2", "location": "onsite"},
    {"person": "i_4", "slot": "slot3", "location": "remote_private"},
    {"person": "i_5", "slot": "slot2", "location": "remote_public"},
    {"person": "i_5", "slot": "slot3", "location": "remote_private"},
    {"person": "i_6", "slot": "slot2", "location": "onsite"},
    {"person": "i_6", "slot": "slot3", "location": "onsite"}
]
# End - data set

def doc_analysis_validation(doc_list):
    participants_union = set()
    for doc in doc_list:
        participants_union = participants_union.union(doc)  

    participant_validity_doc_analysis = {} # Initialize an empty dictionary to store the participant validity
    
    for individual_i in participants_union: # Iterate through each individual (excluding "public")
        if individual_i != "public":  # Exclude "public"
            i_validity = True  # Start with a True assumption
            
            for doc in doc_list: # Use AND operation to combine the conditions
                if doc == doc_list[-1]:
                    i_validity_in_doc = individual_i in doc
                else:
                    i_validity_in_doc = Or("public" in doc, individual_i in doc) # "public" in doc or individual_i in doc
                i_validity = And(i_validity, i_validity_in_doc) # Use AND to combine the conditions for all docs
            participant_validity_doc_analysis[individual_i] = i_validity.simplify() # Evaluate the symbolic expression (True or False) and map to the individual in dictionary
    return participant_validity_doc_analysis

def time_slot_and_participant_analysis(doc_list, participant_validity_doc_analysis, availability_dictionary, meeting_quorum):
    meeting_publicity = And(*[("public" in doc) for doc in doc_list]) # Meeting Publicity - Check if "public" is in each document in doc_list
    time_slots = sorted(set(entry["slot"] for entry in availability_dictionary)) # Extract distinct "slot" values from availability_dictionary
    time_slots_and_participants = {} # Initialize the time_slots_and_participants dictionary
    for slot in time_slots: # Process each time slot
        time_slot = {}  # Empty dictionary for the current time slot

        for individual_i, validity in participant_validity_doc_analysis.items(): # For each individual in participant_validity_doc_analysis
            # Find all the entries for individual_i for the current slot
            individual_entries = [ 
                entry for entry in availability_dictionary
                if entry["person"] == individual_i and entry["slot"] == slot
            ]

            if individual_entries: # If individual is present in the current slot
                location = individual_entries[0]["location"] # Check the location for this individual in the time slot
                
                # Create time_slot_for_individual_i condition:
                # (AND(meeting_publicity, presence in slot) OR (presence in slot AND location))
                presence_condition = Or(
                    And(meeting_publicity, individual_i in [entry["person"] for entry in individual_entries]),
                    And(individual_i in [entry["person"] for entry in individual_entries], Not(location == "remote_public"))
                )

                eligibility = And(validity, presence_condition) # Calculate eligibility for individual_i in this time slot
                
                time_slot[f"{slot}_{individual_i}_eligibility"] = eligibility.simplify() # Add the eligibility result for this individual to the time_slot dictionary
            else:
                time_slot[f"{slot}_{individual_i}_eligibility"] = False # Add "False" as eligibility result if individual is not available in time slot

        time_slots_and_participants[slot] = time_slot # Add the time_slot dictionary to the main dictionary

    return time_slots_and_participants # Return the final result

def meeting_quorum_analysis(time_slots_and_participants, meeting_quorum):
    # Initialize an empty dictionary to store the quorum satisfiability of each slot
    quorum_satisfiability_of_slots = {}

    # Iterate over each slot in the time_slots_and_participants dictionary
    for slot, participants in time_slots_and_participants.items():
        satisfiability_of_slot = False
        
        # Get the list of participant eligibility keys (e.g., 'slot1_i_1_eligibility', etc.)
        participant_keys = list(participants.keys())

        # Iterate through all combinations of meeting_quorum participants
        for combination in combinations(participant_keys, meeting_quorum):
            # Create a condition for the current combination (AND for all participants in the combination)
            eligibility_condition = And(*[participants[participant] for participant in combination])

            # If the condition is satisfied (i.e., all participants in the combination are eligible), update the satisfiability
            satisfiability_of_slot = Or(satisfiability_of_slot, eligibility_condition)

        # Add the result for this slot to the quorum_satisfiability_of_slots dictionary
        quorum_satisfiability_of_slots[slot] = satisfiability_of_slot

    satisfiability_values = list(quorum_satisfiability_of_slots.values()) # Extract satisfiability_of_slot values
    quorum_satisfiability_for_meeting = Or(*[true if val else false for val in satisfiability_values]) # Convert each boolean value into sympy's boolean constants (true/false)
    
    # Return the dictionary containing the satisfiability of each slot
    return quorum_satisfiability_of_slots, quorum_satisfiability_for_meeting

def execute_meeting_organizer():
    doc1 = {"public"}
    doc2 = {"i_2", "i_3", "i_4", "i_5", "i_6"}
    doc3 = {"public"}
    agenda = {"public", "i_1", "i_2", "i_3", "i_4", "i_5"}
    doc_list = [doc1, doc2, doc3, agenda] # !! PASS AGENDA AS LAST ELEMENT !!
    meeting_quorum = 3

    # Participant validation by doc analysis
    participant_validity_doc_analysis = doc_analysis_validation(doc_list)
    print("Participant validity by doc analysis: ", participant_validity_doc_analysis)

    # Time slot and participant analysis
    time_slots_and_participants = time_slot_and_participant_analysis(doc_list, participant_validity_doc_analysis, availability_dictionary, meeting_quorum) 
    for time_slot, individuals in time_slots_and_participants.items(): # Print the result
        print(f"Time Slot: {time_slot}")
        for individual, eligibility in individuals.items():
            print(f"  {individual}: {eligibility}")
    
    
    # Meeting quorum analysis
    quorum_satisfiability_of_slots, quorum_satisfiability_for_meeting = meeting_quorum_analysis(time_slots_and_participants, meeting_quorum)
    for slot, satisfiable in quorum_satisfiability_of_slots.items(): # Print the result
        print(f"Slot: {slot}, Quorum Satisfiability: {satisfiable}")
    print("Quorum satisfiability for meeting: ", quorum_satisfiability_for_meeting)

execute_meeting_organizer()


