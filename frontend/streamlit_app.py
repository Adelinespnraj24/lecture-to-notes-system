import streamlit as st
import requests

st.title("Lecture to Notes System")

text = st.text_area("Enter lecture text:")

if st.button("Summarize"):
    if text:
        response = requests.post(
            "http://127.0.0.1:8000/summarize",
            json={"text": text}
        )

        if response.status_code == 200:
            summary = response.json()["summary"]
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Error from API")
    else:
        st.warning("Please enter text")