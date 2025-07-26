import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("This is simple app to demonstrate the basic functionalties of Streamlit.")

st.sidebar.header("User Input Features")

user_name = st.sidebar.text_input("What is your name?", "Streamlit User")

age = st.sidebar.slider("Select your age", 0, 100, 25)

favourite_color = st.sidebar.selectbox("What is your favourite color?", ["Blue", "Red", "Green", "Yellow", "Pink", "Black"])

# Main page content
st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favourite color is {favourite_color}.")

# Displaying Data
st.subheader("Here's some random data:")

# Create a sample Dataframe
data = pd.DataFrame(
    np.random.randn(10,5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)


if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")