
import streamlit as st

# Set the title of the app
st.title("Product-Audience Form")

# Create text input fields
product = st.text_input("Product")
audience = st.text_input("Audience")

# Create an Enter button
if st.button("Enter"):
    if product and audience:
        st.success(f"You entered:\n- Product: **{product}**\n- Audience: **{audience}**")
    else:
        st.warning("Please fill in both fields before pressing Enter.")
