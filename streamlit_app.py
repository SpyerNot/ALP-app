import streamlit as st
st.title("Our Health App!!")
with st.form(key='know_more_form'):
  st.header("This is a form to get to know more about you!")
  gender = st.selectbox("What is your gender?",["Female","Male"])
  age = st.text_input("Which year are you born?")
  height = st.number_input("What is your height? (in meteres)",0.00,)
  weight = st.number_input("What is your weight? (in kilograms)",0.00,)
  st.form_submit_button("Submit")
height = height * height
bmi = weight / height
if ZeroDivisionError == True:
  st.write("Please put in a valid input")
else:
  pass
if bmi >= 40.0:
  st.write("You are obese")
elif bmi >= 25.0:
  st.write("You are overweight")
elif bmi >=18.5:
  st.write("You are normal")
else:
  st.write("You are underweight")
