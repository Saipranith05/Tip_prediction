import streamlit as st
import joblib 
import pandas as pd
import numpy as np

model = joblib.load("tips1.pkl")

st.title("Prediction of App")
st.image("wallpaper.jpg")

total_bill = st.number_input("Please entre your total_bill:", min_value=10, step=1)
gender = st.selectbox("sex(0:Male, 1:Female)", [0,1])
smoker = st.selectbox("smoker(0:Yes, 1:No)", [0,1])
day = st.selectbox("day(0:Thur, 1:Fri, 2:Sat, 3:Sun)",[0,1,2,3])
time = st.selectbox("time(0:Lunch, 1:Dinner)", [0,1])
size = st.number_input("Please enter your size", min_value=1, step=1)

if st.button('predict'):
    features = np.array([[total_bill, gender, smoker, day, time, size ]])
    output = model.predict(features)
    
    st.write(f"The predicted tip amount is ${output[0]:.2f}")