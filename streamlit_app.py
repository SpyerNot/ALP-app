import streamlit as st

st.title("Our Health App!!")
st.header("This is a form to know more about you!")
gender = st.selectbox("What is your gender?",["Female","Male"])
age = st.text_input("Which year are you born?")
height = st.text_input("What is your height?")
weight = st.text_input("What is your weight?")

