import streamlit as st

# --- PAGE SETUP ---
page_one = st.Page(
	page="views/page1.py",
	title="Meeting Details",
	icon=":material/account_circle:",
	default=True,
)

page_seven = st.Page(
	page="views/page7.py",
	title="Meething Quorum",
	icon=":material/groups:",
)

page_two = st.Page(
	page="views/page2.py",
	title="Schedule Meeting",
	icon=":material/bar_chart:",
)

page_three = st.Page(
	page="views/page3.py",
	title="Add User",
	icon=":material/smart_toy:",
)

page_four = st.Page(
    page="views/page4.py",
    title="Add Group",
    icon=":material/group:",
)

page_five = st.Page(
    page="views/page5.py",
    title="Calendar",
    icon=":material/calendar_month:",
)

page_six = st.Page(
    page="views/page6.py",
    title="Office Locations",
    icon=":material/location_on:",
)



# --- NAVIGATION SETUP [WITHOUT SECTIONS] --- 
#pg = st.navigation(pages=[page_one, page_two, page_three, page_four, page_five])

# --- NAVIGATION SETUP [WITH SECTIONS] --- 
pg = st.navigation({
	"" : [page_one, page_seven, page_two],
	"Admin" : [page_three, page_four, page_five, page_six]
})

with open('styles.css') as f:
	st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

# --- RUN NAVIGATION --- 
pg.run()