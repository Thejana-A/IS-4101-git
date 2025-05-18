import streamlit as st

st.title("Calendar")

# Embed Google Calendar using HTML with English language enforced
calendar_html = """
<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=Asia%2FColombo&title=common%20calendar&showPrint=0&src=amF5YXRoaWxha2Vwb29ybmltYTk5QGdtYWlsLmNvbQ&src=ZW4ubGsjaG9saWRheUBncm91cC52LmNhbGVuZGFyLmdvb2dsZS5jb20&src=cG9vcm5pbWFqYXlhdGhpbGFrZTE5OTlAZ21haWwuY29t&color=%23039BE5&color=%230B8043&color=%23D81B60&hl=en" 
style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>
"""

# Display the calendar using Streamlit's markdown function with unsafe_allow_html
st.markdown(calendar_html, unsafe_allow_html=True)