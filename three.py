import streamlit as st 
st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://holycowvegan.net/wp-content/uploads/2022/09/masala-chai-tea-recipe-11.jpg", width=200)
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Ginger Chai")
    st.image("https://media.istockphoto.com/id/1482828620/photo/clay-tea-cup-being-hold-in-the-hand.jpg?s=612x612&w=0&k=20&c=zULj4iZBUdV4TjzeYQLBr3QGD_1lPRuGtnD1i57p-A8=", width =200)
    vote2 = st.button("Vote for Ginger Chai")

if vote1:
    st.success("You voted for Masala Chai! 🍵")
elif vote2:
    st.success("You voted for Ginger Chai! 🍵")

name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("Select your favorite chai:", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"])

st.write(f"Hello {name}, you selected {tea} as your favorite chai!")

with st.expander("See Chai Facts"):
    st.write("""
    - Chai is a popular beverage in India and around the world.
    - It is made by brewing tea with a mixture of aromatic spices and herbs.
    - Common spices include cardamom, cinnamon, ginger, cloves, and black pepper.
    - Chai is often enjoyed with milk and sugar.
    """)

st.markdown("---")
st.header("Chai Feedback Form")
feedback = st.text_area("What do you think about chai?")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")