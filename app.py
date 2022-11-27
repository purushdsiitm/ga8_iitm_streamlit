import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Division of two numbers

This app takes two number's as input, and divide the First number with Second number and shows result as output

""")

#Get Input

st.header('Input Parameters')

def user_input_features():
  first_number = st.number_input("Enter First Number",min_value=0.00)
  second_number = st.number_input("Enter Second Number",min_value=1.00)

  data = {'First_Number':first_number,
          'Second_Number':second_number
         }
  
  features = pd.DataFrame(data,index=[0])
  return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df.to_dict())

st.subheader("Result of Division of two numbers is:")

result = (df['First_Number']/df['Second_Number'])
st.write(result)
