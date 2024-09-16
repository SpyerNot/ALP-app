import streamlit as st

st.title("Our Health App!!")
with st.form(key='Get to know more about you!'):
  gender = st.selectbox("What is your gender?",["Female","Male"])
  age = st.text_input("Which year are you born?")
  height = st.text_input("What is your height?")
  weight = st.text_input("What is your weight?")
  st.form_submit_button("Submit")
