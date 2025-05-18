import streamlit as st
from typing import Set, Tuple

def get_allowed_participants(
    agenda_emails: Set[str], 
    intersected_emails: Set[str], 
    meeting_type: str, 
    meeting_type_for_non_agenda: str
) -> Tuple[Set[str], str]:
    """
    Determines the allowed participants for a meeting and provides a message explaining the decision.

    - Always allows intersected emails.
    - If an email is in the agenda but not in the intersection, they are not allowed.

    Args:
        agenda_emails (Set[str]): Emails from the Agenda document.
        intersected_emails (Set[str]): Emails common across all permissioned documents.

    Returns:
        Tuple[Set[str], str]: A set of allowed participants and an explanation message.
    """
    
    #allowed_participants = intersected_emails  # Only intersected emails are allowed
    
    ## Find agenda participants who are NOT in the intersection (they are NOT allowed)
    #not_allowed_participants = agenda_emails - intersected_emails

    # Only those present in both agenda and intersected emails
    allowed_participants = agenda_emails & intersected_emails
    
    # Participants who are in either set but not both
    #if(agenda_emails > intersected_emails):
    #    not_allowed_participants = agenda_emails - allowed_participants
    #else if (agenda_emails < intersected_emails):
    #    not_allowed_participants = allowed_participants - agenda_emails

    not_allowed_participants = (agenda_emails | intersected_emails) - allowed_participants
    #not_allowed_participants = agenda_emails - allowed_participants

    agenda_not_allowed_participants = agenda_emails - allowed_participants
    intersection_not_allowed_participants = intersected_emails - allowed_participants


    if meeting_type == "Public":
        if meeting_type_for_non_agenda == "Public Meeting":
            # If it's public and any user can attend, we allow all agenda participants
            allowed_participants = intersected_emails | agenda_emails
            st.session_state.final_meeting_type = "Public"
            st.success("Attached documents are also public")
            message = (
                "✅ This is a public meeting, and **any user can attend**.\n\n"
                + "\n✅ All agenda and documents participants are allowed to join.\n\n"
            )
            message += (
                "✅ **Allowed participants (in both agenda and document access):**\n\n"
                + "\n".join([f'`{email}`' for email in allowed_participants])
            )
        else:
            # If not, only the intersected participants can join
            st.session_state.final_meeting_type = "Private"
            st.warning("Attached documents are not all public, only allowed participants can attend")
            if not not_allowed_participants:
                message = "✅ All agenda and documents participants are allowed to the meeting."
            else:
                message = (
                    "⚠️ **The following participants are not allowed based on the current rules:**\n\n"
                )
                if agenda_not_allowed_participants:
                    message += (
                        "❌ **Agenda participants NOT found in document access:**\n"
                        + "\n".join([f'`{email}`' for email in agenda_not_allowed_participants]) + "\n\n"
                    )
                    st.warning("This meeting cannot be done with suggested agenda participants")
                if intersection_not_allowed_participants:
                    message += (
                        "❌ **Document-access participants NOT listed in the agenda:**\n"
                        + "\n".join([f'`{email}`' for email in intersection_not_allowed_participants]) + "\n\n"
                    )
                message += (
                    "✅ **Allowed participants (in both agenda and document access):**\n"
                    + "\n".join([f'`{email}`' for email in allowed_participants])
                )
    else:
        st.session_state.final_meeting_type = "Private"
        if not not_allowed_participants:
            message = "✅ All agenda and documents participants are allowed to the meeting."
        else:
            message = (
                "⚠️ **Some participants do not meet the necessary criteria:**\n\n"
            )
            if agenda_not_allowed_participants:
                message += (
                    "❌ **Agenda participants NOT found in document access:**\n"
                    + "\n".join([f'`{email}`' for email in agenda_not_allowed_participants]) + "\n\n"
                )
                st.error("This meeting cannot be done with suggested agenda participants")
            if intersection_not_allowed_participants:
                message += (
                    "❌ **Document-access participants NOT listed in the agenda:**\n"
                    + "\n".join([f'`{email}`' for email in intersection_not_allowed_participants]) + "\n\n"
                )
            message += (
                "✅ **Allowed participants (in both agenda and document access):**\n"
                + "\n".join([f'`{email}`' for email in allowed_participants])
            )

    return allowed_participants, message
