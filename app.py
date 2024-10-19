import streamlit as st
import joblib
import numpy as np

model = joblib.load("tips.pkl")

st.title("App of Prediction")
st.image("wallpaper.jpg")

#total_bill = st.number_input("Please enter your total_bill:", min_value=0, step=0)
#gender = st.selectbox('sex(0:Male, 1:Female)', [0,1])
#smoker = st.selectbox('smoker(0:Yes, 1:No)', [0,1])
#day = st.selectbox('day(0:Thur, 1:Fri, 2:Sat, 3:Sun)', [0,1,2,3])
#time = st.selectbox('time(0:Lunch, 1:Dinner)', [0,1])
#size = st.number_input("Please enter size:", min_value=0, step=1)


#if st.button("predict"):
 #   features = np.array([[total_bill,gender,smoker,day,time,size]])
  #  result = model.predict(features)
   # st.write(f"The predicted tip amount is ${result[0]:.2f}")
   
total_bill = st.number_input("Please enter your total_bill:", min_value=0.0, step=0.01)
gender = st.selectbox('sex (Select: 0 for Male, 1 for Female)', [None, 0, 1], index=0)
smoker = st.selectbox('smoker (Select: 0 for Yes, 1 for No)', [None, 0, 1], index=0)
day = st.selectbox('day (select : 0 for Thur, 1 for Fri, 2 for Sat, 3 for Sun)', [None, 0, 1, 2, 3], index=0)
time = st.selectbox('time (Select: 0 for Lunch, 1 for Dinner)', [None, 0, 1], index=0)
size = st.number_input("Please enter size:", min_value=0, step=1)

if st.button("predict"):
    # Ensure user selected all inputs
    if None in (gender, smoker, day, time):
        st.write("Please select values for all inputs.")
    else:
        features = np.array([[total_bill, gender, smoker, day, time, size]])
        result = model.predict(features)
        st.write(f"The predicted tip amount is ${result[0]:.2f}")