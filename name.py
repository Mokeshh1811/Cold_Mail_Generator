import streamlit as st
st.title("📧Cold Mail Generator")
url_input=st.text_input("Enter a URL:",value="https://jobs.nike.com/?jobSearch=true&jsOffset=0&jsSort=posting_start_date&jsLanguage=en")
submit_button=st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, Iam From ABCD ", language='markdown')