import streamlit as st
import requests

st.title("Live currency converter")
amount = st.number_input("Enter amount to convert", min_value=0.0, value=1.0)
from_currency = st.selectbox("From currency", ["USD", "EUR", "GBP", "INR", "JPY"])
to_currency = st.selectbox("To currency", ["USD", "EUR", "GBP", "INR", "JPY"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    if "rates" in data:
        rate = data["rates"].get(to_currency)
        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error("Conversion rate not found.")
    else:
        st.error("Failed to fetch exchange rates.")