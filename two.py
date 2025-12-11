import streamlit as st 
st.title("Chai maker App")

if st.button("Make me a Chai!"):
    st.text("Brewing your perfect cup of chai... ☕")
    st.balloons()
    st.success("Your chai is ready! Enjoy! 🍵")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added! Spicing things up!")

tea_type = st.radio("Choose your tea base:", ("Black Tea", "Green Tea", "Herbal Tea"))
st.write(f"You selected: {tea_type} as your tea base.")
flavour = st.selectbox("Select a flavour:", ["Ginger", "Cardamom", "Tulsi", "Saffron"])
st.write(f"You selected: {flavour} flavour.")
sugar = st.slider("Select sugar level (spoons):", 0, 5, 2)
st.write(f"Sugar level set to: {sugar} spoons.")

cups = st.number_input("Number of cups to brew:", min_value=1, max_value=10, value=1)
st.write(f"Preparing to brew {cups} cup(s) of chai.")

name = st.text_input("Enter your name for the chai order:")
if name:
    st.write(f"Thank you, {name}! Your chai order is being prepared.")

dob = st.date_input("Enter your date of birth:")
st.write(f"Your date of birth is: {dob}")
st.text_area("Any special instructions for your chai?")