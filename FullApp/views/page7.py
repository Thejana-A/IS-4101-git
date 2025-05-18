import streamlit as st

# Ensure the session state variable exists
if "final_meeting_type" not in st.session_state:
    st.error("Add meeting details first.")
else:
    final_meeting_type = st.session_state.final_meeting_type
    allowed = st.session_state.allowed_participants

    if final_meeting_type == "Private":
        if "allowed_participants" in st.session_state:
            #allowed = st.session_state.allowed_participants
            st.warning(
                "This is a private meeting with allowed participants with private locations.\n\n"
                + "**Allowed participants are:**\n"
                + ", ".join([f'`{email}`' for email in allowed])
            )
        #st.warning("This is a private meeting with allowed participants with private locations. \n\n allowed participants are  ")
    else:
        st.success(
            "This is a public meeting. Anyone can join from any location.\n\n" 
            + "**Filtered participants from document analysis:** " 
            + ", ".join([f'`{email}`' for email in allowed])
        )

    # Ask about quorum
    st.title("Do we want a meeting quorum?")
    quorum_required = st.radio(
        "Is a quorum required for this meeting?",
        ("Yes", "No"),
        key="quorum_required"
    )

    # If quorum is required, show a number input field
    if st.session_state.quorum_required == "Yes":
        quorum_number = st.number_input(
            "Enter the minimum number of participants required for quorum:",
            min_value=0,
            step=1,
            #key="quorum_number"
        )
        st.session_state.quorum_number = quorum_number

        # Optionally confirm it
        #st.info(f"Quorum set to **{int(st.session_state.quorum_number)}** participants.")

        if quorum_number > len(allowed) and final_meeting_type != "Public":
            st.error("Quorum is higher than the permitted participants.")
        else:
            if st.button("Proceed with meeting scheduling?"):
                st.switch_page("views/page2.py")

    else:
        st.session_state.quorum_number = None  # Clear it if quorum not required
        if st.button("Proceed with out meeting Quorum?"):
                st.switch_page("views/page2.py")