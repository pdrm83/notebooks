import streamlit as st
import requests

WEBHOOK_URL = "http://n8n.localhost/webhook/109891a6-7fb1-443c-a753-f34f6e6f715d"

st.title("Send Product & Audience to n8n")

product = st.text_input("Product")
audience = st.text_input("Audience")

if st.button("Enter"):
    if product and audience:
        payload = {
            "product": product,
            "audience": audience
        }

        try:
            response = requests.post(WEBHOOK_URL, json=payload, verify=False)
            if response.status_code == 200:
                st.success("Data sent to n8n successfully!")
            else:
                st.error(f"Failed to send data. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both fields before submitting.")
