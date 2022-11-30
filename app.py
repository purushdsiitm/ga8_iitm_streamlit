import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Division of two numbers

This app takes two number's as input, and divide the First number with Second number and shows result as output

""")

#Get Input

st.header('Input Parameters')

first_number = st.number_input("Enter First Number")
second_number = st.number_input("Enter Second Number")

st.subheader("User Input Parameters")
st.write({ 'first_number': first_number,
           'second_number': second_number })

st.subheader("Result of Division of two numbers is:")
if second_number == 0.0:
  st.write("Second number can not be zero. Please enter valid number")
else:
  result = (first_number/second_number)
  st.write(result)
