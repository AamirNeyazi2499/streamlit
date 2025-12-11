import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with Streamlit")
st.text("Welcome to my first Chai Streamlit application!")
st.write("Choose your fav. variety of chai: ")

chai = st.selectbox("Select Chai:", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"])
st.write(f"You selected: {chai}. Excellent choice!")
st.success("Enjoy your cup of chai! ☕")



