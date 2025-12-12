import streamlit as st
import pandas as pd

st.title("Chai sales dashboard")

file = st.file_uploader("Upload your sales data CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Statistics")
    st.write(df.describe())

if file:
    cities = df['City'].unique()
    selected_city = st.selectbox("Select a city to filter data", cities)
    filtered_df = df[df['City'] == selected_city]
    st.dataframe(filtered_df)