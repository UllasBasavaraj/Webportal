import streamlit as st

st.write("Hello world")
name = st.text_input("What is your name?")

st.write(f"Welcome to streamlit : {name}")

submit = st.button("Submit")

st.text_area("This is a text area")

st.bar_chart