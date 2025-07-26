# 1.Import streamlit
import streamlit as st

# 2. Add a title to your app
st.title("My First Streamlit App created by Prachi Singare")

# 3. add some text
st.write("Welcome! This app calculates the square of number.")


st.header("Select a number")
number = st.slider("Pick a number", 0, 100, 25)  # min, max , default


st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")

