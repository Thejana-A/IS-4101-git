from sympy import symbols  # Correct import for symbols
from sympy.logic.boolalg import Or, And, Not, simplify_logic
from sympy import true, false  # For boolean constants
from itertools import combinations

import sympy
import sys

# Start - data set
# Availabile time slots and locations of participants
availability_dictionary = [
    {"person": "i_1", "slot": "slot1", "location": "onsite"},
    {"person": "i_1", "slot": "slot2", "location": "onsite"},
    {"person": "i_1", "slot": "slot3", "location": "onsite"},
    {"person": "i_1", "slot": "slot4", "location": "remote_private"},
    {"person": "i_2", "slot": "slot1", "location": "onsite"},
    {"person": "i_2", "slot": "slot2", "location": "remote_private"},
    {"person": "i_2", "slot": "slot3", "location": "remote_private"},
    {"person": "i_2", "slot": "slot4", "location": "remote_public"},
    {"person": "i_3", "slot": "slot1", "location": "onsite"},
    {"person": "i_3", "slot": "slot2", "location": "onsite"},
    {"person": "i_3", "slot": "slot3", "location": "onsite"},
    {"person": "i_3", "slot": "slot4", "location": "onsite"},
    {"person": "i_4", "slot": "slot1", "location": "onsite"},
    {"person": "i_4", "slot": "slot2", "location": "onsite"},
    {"person": "i_4", "slot": "slot3", "location": "remote_private"},
    {"person": "i_4", "slot": "slot4", "location": "remote_private"},
    {"person": "i_5", "slot": "slot2", "location": "remote_public"},
    {"person": "i_5", "slot": "slot3", "location": "remote_private"},
    {"person": "i_6", "slot": "slot2", "location": "onsite"},
    {"person": "i_6", "slot": "slot3", "location": "onsite"},
    {"person": "i_7", "slot": "slot5", "location": "onsite"},
    {"person": "i_7", "slot": "slot6", "location": "onsite"},
    {"person": "i_7", "slot": "slot7", "location": "onsite"},
    {"person": "i_7", "slot": "slot8", "location": "onsite"},
    {"person": "i_7", "slot": "slot9", "location": "onsite"},
    {"person": "i_7", "slot": "slot10", "location": "onsite"},
    {"person": "i_7", "slot": "slot11", "location": "onsite"}
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
    time_slots = sorted(set(entry["slot"] for entry in availability_dictionary if entry["person"] in participant_validity_doc_analysis)) # Extract distinct "slot" values from availability_dictionary for participants in doc_union
    #time_slots = sorted(set(entry["slot"] for entry in availability_dictionary))
    time_slots = sorted(time_slots, key=lambda x: int(x[4:]))  # Sorting based on numeric part after 'slot'


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
                meeting_publicity = And(*[("public" in doc) for doc in doc_list]) # Meeting Publicity - Check if "public" is in each document in doc_list 
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

#def earliest_slot_selection(quorum_satisfiability_of_slots):
def find_earliest_eligible_slot(quorum_satisfiability_of_slots):
    # Dynamically define symbols for slots based on the input dictionary keys
    slots = symbols(list(quorum_satisfiability_of_slots.keys()))

    # Map symbols to input values
    symbol_values = {slot: quorum_satisfiability_of_slots[name] for slot, name in zip(slots, quorum_satisfiability_of_slots.keys())}

    # Build the circuit logic dynamically
    earliest_eligibles = []  # To store the earliest eligible conditions

    for i, slot in enumerate(slots):
        if i == 0:
            # The first slot is directly eligible
            earliest_eligibles.append(slot)
        else:
            # All previous slots must be false
            previous_conditions = [Not(earliest_eligibles[j]) for j in range(i)]
            # Current slot's condition
            condition = And(And(*previous_conditions), slot)
            earliest_eligibles.append(condition)

    # Optionally, print each slot's eligibility
    for i, condition in enumerate(earliest_eligibles, start=1):
        print(f"Slot {i} eligibility as earliest slot:", condition.subs(symbol_values))

    # Combine all cases into a single result
    result = Or(*earliest_eligibles)
    # Evaluate the result with the input values
    evaluated_result = result.subs(symbol_values)
    # Print the evaluated result
    print("Existence of an earliest elible time slot:", evaluated_result)

def select_meeting_mode(time_slots_and_participants, quorum_satisfiability_of_slots):
    availability_dict = {}
    for entry in availability_dictionary:
        availability_dict[(entry['person'], entry['slot'])] = entry['location']

    results = {}

    for slot_x, participants in time_slots_and_participants.items():
        slot_x_onsite = {}
        slot_x_online = {}

        # Populate onsite and online dictionaries
        for participant, eligibility in participants.items():
            person = '_'.join(participant.split('_')[1:3])
            if (person, slot_x) in availability_dict:
                if availability_dict[(person, slot_x)] == 'onsite':
                    onsite = True
                else:
                    onsite = False
                slot_x_onsite[participant] = eligibility and onsite
                slot_x_online[participant] = eligibility and not onsite
            else:
                slot_x_onsite[participant] = eligibility and False
                slot_x_online[participant] = eligibility and False
        

        # Determine if the slot is onsite or hybrid
        slot_x_is_onsite_or_hybrid = False
        for comb in combinations(slot_x_onsite.values(), 2):
            slot_x_is_onsite_or_hybrid = slot_x_is_onsite_or_hybrid or (comb[0] and comb[1])

        # Eligibility for online meeting
        eligibility_online = (not slot_x_is_onsite_or_hybrid) and quorum_satisfiability_of_slots[slot_x]

        # Possibility for hybrid meeting
        possibility_hybrid = False
        quorum_hybrid_onsite = quorum_satisfiability_of_slots[slot_x] and slot_x_is_onsite_or_hybrid

        for online_presence in slot_x_online.values():
            possibility_hybrid = possibility_hybrid or online_presence

        # Eligibility for hybrid meeting
        eligibility_hybrid = possibility_hybrid and quorum_hybrid_onsite

        # Eligibility for onsite meeting
        eligibility_onsite = (not eligibility_hybrid) and quorum_hybrid_onsite

        # Store results for the slot
        results[slot_x] = {
            'eligibility_online': eligibility_online,
            'eligibility_hybrid': eligibility_hybrid,
            'eligibility_onsite': eligibility_onsite
        }
    print("Meeting mode Eligibility:")
    for slot, eligibility in results.items():
        print(f"{slot.capitalize()}:")
        for mode, status in eligibility.items():
            mode_formatted = mode.replace('_', ' ').capitalize()
            print(f"  {mode_formatted}: {'True' if status else 'False'}")


def execute_meeting_organizer():
    doc1 = {"public"}
    doc2 = {"i_2", "i_3", "i_4", "i_5", "i_6"}
    doc3 = {"public"} 
    agenda = {"public", "i_1", "i_2", "i_3", "i_4", "i_5"}
    doc_list = [doc1, doc2, doc3, agenda] # !! PASS AGENDA AS LAST ELEMENT !!
    meeting_quorum = 3

    if meeting_quorum >= 2:
        # Participant validation by doc analysis
        print("Algorithm 01")
        participant_validity_doc_analysis = doc_analysis_validation(doc_list)
        print("Participant validity by doc analysis: ", participant_validity_doc_analysis)

        print("\nAlgorithm 02")
        # Time slot and participant analysis
        time_slots_and_participants = time_slot_and_participant_analysis(doc_list, participant_validity_doc_analysis, availability_dictionary, meeting_quorum) 
        for time_slot, individuals in time_slots_and_participants.items(): # Print the result
            print(f"Time Slot: {time_slot}")
            for individual, eligibility in individuals.items():
                print(f"  {individual}: {eligibility}")
        
        print("\nAlgorithm 03")
        # Meeting quorum analysis
        quorum_satisfiability_of_slots, quorum_satisfiability_for_meeting = meeting_quorum_analysis(time_slots_and_participants, meeting_quorum)
        for slot, satisfiable in quorum_satisfiability_of_slots.items(): # Print the result
            print(f"Slot: {slot} - Quorum Satisfiability: {satisfiable}")
        print("Quorum satisfiability of slots: ", quorum_satisfiability_of_slots)
        print("Quorum satisfiability for meeting: ", quorum_satisfiability_for_meeting)

        print("\nAlgorithm 04")
        find_earliest_eligible_slot(quorum_satisfiability_of_slots)

        print("\nAlgorithm 05")
        select_meeting_mode(time_slots_and_participants, quorum_satisfiability_of_slots)
    else:
        print("Meeting quorum should be 2 or greater than 2")


execute_meeting_organizer()

print("Python version: ", sys.version)
print("Sympy version: ", sympy.__version__)



