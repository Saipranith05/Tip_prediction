import streamlit as st
import joblib
import numpy as np

model = joblib.load("tips.pkl")