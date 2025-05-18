import pandas as pd
import streamlit as st

def filter_permissioned_events(filtered_events, intersected_emails, meeting_type):
    """
    Filters events to include only those of users present in intersected_emails.
    Applies meeting type rules (Private meetings can only be attended by 'Work' or 'Home' users).
    Groups events by user for structured display.
    """
    filtered_list = [
        event for event in filtered_events
        if event["User Email"] in intersected_emails and 
        (meeting_type != "Private" or event["Location Label"] in {"Work", "Home"})
    ]

    # If no events matched, return None
    if not filtered_list:
        return None

    # Convert filtered list to DataFrame
    df = pd.DataFrame(filtered_list)

    # Ensure required columns exist before sorting
    expected_columns = {"User Email", "Date", "Time Slot", "Location", "Location Label"}
    if not expected_columns.issubset(df.columns):
        raise ValueError("One or more expected columns are missing in the events data.")

    # Sort and order columns
    df.sort_values(by=["User Email", "Date", "Time Slot"], inplace=True)
    column_order = ["User Email", "Date", "Time Slot", "Location", "Location Label"]
    df = df[column_order]

    return df

#def find_earliest_meeting_time(new_events, intersected_emails, quorum):
#    """
#    Finds and prints the earliest available time slot where all users in intersected_emails are present.
#    """
#    df = pd.DataFrame(new_events)  # Convert events to DataFrame
    
#    # Sort to ensure we check the earliest times first
#    df.sort_values(by=["Date", "Time Slot"], inplace=True)

#    # Group by Date and Time Slot
#    grouped = df.groupby(["Date", "Time Slot"])  

#    # Iterate over each unique time slot
#    for (date, time_slot), group in grouped:
#        users_in_slot = set(group["User Email"])  # Users available in this slot

#        # Check if all required users are available
#        if set(intersected_emails).issubset(users_in_slot):
#            st.success(f"✅ Recommended Meeting Time: {date} at {time_slot}")
#            return  # Stop after finding the earliest slot

#    # If no common slot is found
#    st.warning("⚠️ No common time slot available for all selected participants.")

#def find_earliest_meeting_time(new_events, intersected_emails, quorum):
#    """
#    Finds and displays all time slots where quorum number of participants are available.
#    Also indicates how many participants are available above the quorum.
#    """
#    df = pd.DataFrame(new_events)

#    # Sort to ensure earliest times are checked first
#    df.sort_values(by=["Date", "Time Slot"], inplace=True)

#    # Group by Date and Time Slot
#    grouped = df.groupby(["Date", "Time Slot"])

#    options_found = []

#    for (date, time_slot), group in grouped:
#        users_in_slot = set(group["User Email"])
#        present_users = users_in_slot.intersection(set(intersected_emails))
#        count_present = len(present_users)

#        if count_present >= quorum:
#            surplus = count_present - quorum
#            options_found.append({
#                "Date": date,
#                "Time Slot": time_slot,
#                "Available Participants": count_present,
#                "Surplus Over Quorum": surplus
#            })

#    if options_found:
#        result_df = pd.DataFrame(options_found)
#        st.success("✅ Time slots where quorum is satisfied:")
#        st.dataframe(result_df)
        
#        # Recommend the best earliest time slot
#        best_option = result_df.iloc[0]
#        st.info(f"🕒 Recommended: {best_option['Date']} at {best_option['Time Slot']} "
#                f"(Quorum +{best_option['Surplus Over Quorum']})")
#    else:
#        st.warning("⚠️ No time slots satisfy the quorum requirement.")

#def find_earliest_meeting_time(new_events, intersected_emails, quorum):
#    """
#    Finds and displays all time slots where quorum number of participants are available.
#    Also indicates how many participants are available above the quorum,
#    and the most secure location type among the participants.
#    """
#    df = pd.DataFrame(new_events)

#    # Define location security ranking (lower number = more secure)
#    security_rank = {
#        "Work": 1,
#        "Home": 2,
#        "Remote Public": 3
#    }

#    # Sort to ensure earliest times are checked first
#    df.sort_values(by=["Date", "Time Slot"], inplace=True)

#    # Group by Date and Time Slot
#    grouped = df.groupby(["Date", "Time Slot"])

#    options_found = []

#    for (date, time_slot), group in grouped:
#        users_in_slot = set(group["User Email"])
#        present_users = users_in_slot.intersection(set(intersected_emails))
#        count_present = len(present_users)

#        if count_present >= quorum:
#            # Filter to only rows from present users
#            present_group = group[group["User Email"].isin(present_users)]

#            # Determine the most secure location from present users
#            present_group["Security Rank"] = present_group["Location Label"].map(security_rank)
#            best_security_rank = present_group["Security Rank"].min()
#            best_location_label = present_group[present_group["Security Rank"] == best_security_rank]["Location Label"].iloc[0]

#            surplus = count_present - quorum

#            options_found.append({
#                "Date": date,
#                "Time Slot": time_slot,
#                "Available Participants": count_present,
#                "Surplus Over Quorum": surplus,
#                "Most Secure Location": best_location_label
#            })

#    if options_found:
#        result_df = pd.DataFrame(options_found)
#        st.success("✅ Time slots where quorum is satisfied:")
#        st.dataframe(result_df)

#        # Recommend the best earliest time slot
#        best_option = result_df.iloc[0]
#        st.info(f"🕒 Recommended: {best_option['Date']} at {best_option['Time Slot']} "
#                f"(Quorum +{best_option['Surplus Over Quorum']}) | "
#                f"🔒 Most Secure: {best_option['Most Secure Location']}")
#    else:
#        st.warning("⚠️ No time slots satisfy the quorum requirement.")

def find_earliest_meeting_time(new_events, intersected_emails, quorum):
    """
    Finds and displays time slots where quorum is satisfied.
    Each option includes participant count, surplus, and average security level based on their Location Label.
    The best slot is selected based on highest group security (lowest average score) and earliest time.
    """
    if quorum is None or quorum == 0:
        quorum = 2

    # Security ranking
    security_rank = {
        "Work": 1,
        "Home": 2,
        "Remote Public": 3
    }

    df = pd.DataFrame(new_events)
    df.sort_values(by=["Date", "Time Slot"], inplace=True)

    grouped = df.groupby(["Date", "Time Slot"])

    options_found = []

    for (date, time_slot), group in grouped:
        users_in_slot = set(group["User Email"])
        present_users = users_in_slot.intersection(set(intersected_emails))
        count_present = len(present_users)

        if count_present >= quorum:
            # Filter only intersected participants
            present_group = group[group["User Email"].isin(present_users)].copy()

            # Map location labels to security scores
            present_group["Security Score"] = present_group["Location Label"].map(security_rank)

            # Compute average score of this group
            avg_security_score = present_group["Security Score"].mean()

            surplus = count_present - quorum

            options_found.append({
                "Date": date,
                "Time Slot": time_slot,
                "Available Participants": count_present,
                "Surplus Over Quorum": surplus,
                "Average Security Score": avg_security_score,
                "Location Labels": list(present_group["Location Label"])
            })

    if options_found:
        result_df = pd.DataFrame(options_found)

        # Sort by security score (ascending) then by Date & Time Slot
        result_df.sort_values(by=["Average Security Score", "Date", "Time Slot"], inplace=True)
        #result_df.sort_values(by=["Date", "Time Slot"], inplace=True)

        st.success("✅ Time slots where quorum is satisfied (ranked by security):")
        st.dataframe(result_df)

        # Show recommended slot
        best = result_df.iloc[0]
        st.info(f"🔒 Recommended: {best['Date']} at {best['Time Slot']} "
                f"(Avg Security: {best['Average Security Score']:.2f}, "
                f"Surplus: {best['Surplus Over Quorum']})")
    else:
        st.warning("⚠️ No time slots satisfy the quorum requirement.")