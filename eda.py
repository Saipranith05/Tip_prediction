import streamlit as st
import mysql.connector
import numpy as np
import joblib

model = joblib.load("logistic.pkl")

def connect_to_database():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Saipranith@2003"
        database = "heart_attack"
    )