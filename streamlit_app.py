import streamlit as st

st.title("Our Health App!!")
with st.form(key='know_more_form'):
  st.header("This is a form to get to know more about you!")
  gender = st.selectbox("What is your gender?",["Female","Male"])
  age = st.text_input("Which year are you born?")
  height = st.text_input("What is your height? (in meters)")
  weight = st.text_input("What is your weight? (in kilograms)")
  st.form_submit_button("Submit")
height = float(height) * float(height)
bmi = float(weight) / height
if bmi >= 40.0:
  print("You are obese")
elif bmi >= 25.0:
  print("You are overweight")
elif bmi >=18.5:
  print("You are normal")
else:
  print("You are underweight")
