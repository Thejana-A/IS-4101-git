import streamlit as st
import pandas as pd
import docx2txt
import pdfplumber

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.subheader("Hi im Poornima")
st.title("Research")

st.sidebar.success("Side Bar Options")

docx_file = st.file_uploader("Upload Document", type=["pdf","docx","txt"])
if st.button("Process"):
    if docx_file is not None:
        file_details = {"filename":docx_file.name, "filetype":docx_file.type, "filesize":docx_file.size}
        st.write(file_details)

        if docx_file.type == "text/plain":
            #Read as bytes
            #raw_text = docx_file.read()
            #st.write(raw_text) #works but in bytes
            #st.text(raw_text) #docs work as expected

            #read as string(decodes bytes to string)
            raw_text = str(docx_file.read(), "utf-8")
            st.write(raw_text)
            #st.text(raw_text) #This works as well

        elif docx_file.type == "application/pdf" :
            try : 
                with pdfplumber.open(docx_file) as pdf:
                    pages =  pdf.pages[0]
                    st.write(pages.extract_text())
            except :
                st.write("None")

        else : 
            raw_text = docx2txt.process(docx_file)
            st.write(raw_text)


#To run 
# python -m streamlit run app.py