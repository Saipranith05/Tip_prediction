import streamlit as st
import mysql.connector
import numpy as np
import joblib

model = joblib.load("logistic.pkl")

def connect_to_database():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Saipranith@2003",
        database = "heart_attack"
    )
    

st.title("Heart Disease Prediction")
    
age = st.number_input('Please mention your age', min_value=1, max_value=120)
sex = st.selectbox('sex(0:Female, 1:Male)',[0,1])
bp = st.number_input('Blood pressure(bp)', min_value=40, max_value=200)
cholesterol = st.number_input('cholesterol(mg/dl)', min_value=50, max_value=600)
    
if st.button("predict"):
        features = np.array([[age, sex, bp, cholesterol]])
        prediction = model.predict(features)[0]
        st.write(f"Prediction of heart disease: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}")
        
        
db=connect_to_database()
cursor = db.cursor()

query = """
insert into user_inputs(age, sex, bp, cholesterol, heart_disease)
values(%s, %s, %s, %s, %s)
"""

cursor.execute (query, (age, sex, bp, cholesterol, int(prediction)))

db.commit()
st.write("Data save to the Database")
cursor.close()
db.close

