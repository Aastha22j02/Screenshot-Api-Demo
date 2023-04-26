import requests
import streamlit as st

screenshot_url = st.secrets['screenshot-api-group']['screenshot-api']

st.title("Website Screenshot")

url = st.text_input("Enter a URL")

if url:
    response = requests.get(f"{screenshot_url}={url}")
    if response.status_code == 200:
        st.image(response.content)
    else:
        st.error("Failed to retrieve screenshot")
