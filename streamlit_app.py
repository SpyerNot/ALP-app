import streamlit as st

st.title("Our Health App!!")
with st.form(key='know_more_form'):
  st.header("This is a form to get to know more about you!")
  gender = st.selectbox("What is your gender?",["Female","Male"])
  age = st.text_input("Which year are you born?")
  height = st.number_input("What is your height?",0.01,2.01)
  weight = st.number_input("What is your weight?",0.01,200.1)
  st.form_submit_button("Submit")
height = height * height
bmi = weight / height
if bmi >= 40.0:
  print("You are obese")
elif bmi >= 25.0:
  print("You are overweight")
elif bmi >=18.5:
  print("You are normal")
else:
  print("You are underweight")
