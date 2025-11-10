import streamlit as st
import pandas as pd
import joblib
from preprocessing import data_prep

model = joblib.load('car price\model.pkl')
encoder = joblib.load('car price\encoder.pkl')

st.markdown("""
    <style>
    /* General background */
    body {
        background-color: #f8fff8;
    }

    /* === Number Input Styling === */
    div[data-baseweb="input"] > div {
        border-radius: 10px !important;
        border: 2px solid #00b300 !important;
        box-shadow: 0 0 10px #00ff00 !important;
        transition: all 0.3s ease-in-out;
    }

    div[data-baseweb="input"] > div:hover {
        border-color: #00ff66 !important;
        box-shadow: 0 0 15px #00ff66 !important;
    }

    /* === Selectbox Styling === */
    div[data-baseweb="select"] {
        border-radius: 10px !important;
        border: 2px solid #00b300 !important;
        box-shadow: 0 0 10px #00ff00 !important;
        transition: all 0.3s ease-in-out;
    }

    div[data-baseweb="select"]:hover {
        border-color: #00ff66 !important;
        box-shadow: 0 0 15px #00ff66 !important;
    }

    /* === Title === */
    h1 {
        color: #006600;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }

    /* === Button Styling === */
    div.stButton > button {
        background-color: #00b300;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6em 2em;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #009900;
        box-shadow: 0 0 10px #00ff66;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Car Price Prediction App")

st.write("Enter car details to predict the price:")

levy = st.number_input("Levy", min_value=0, max_value=100000, value=2500)
year = st.number_input("Production Year", min_value=1990, max_value=2025, value=2018)
ev = st.number_input("Engine Volume (e.g., 2.0)", min_value=0.0, max_value=10.0, value=2.0)
mileage = st.number_input("Mileage (in km)", min_value=0, max_value=5000000, value=50000)
cylinders = st.number_input("Cylinders", min_value=1, max_value=12, value=4)
airbags = st.number_input("Airbags", min_value=0, max_value=16, value=4)

cat = st.selectbox("Category", ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup'])
li = st.selectbox("Leather Interior", ["Yes", "No"])
fuel = st.selectbox("Fuel Type", ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG',
       'Hydrogen'])
gear = st.selectbox("Gear Box Type", ['Automatic', 'Tiptronic', 'Variator', 'Manual'])
wheel = st.selectbox("Drive Wheels", ['4x4', 'Front', 'Rear'])
turbo = st.selectbox("Turbo", ["Yes", "No"])

if st.button("Predict Price"):
    X_new = data_prep(
        encoder=encoder,
        levy=levy, year=year, ev=ev, mileage=mileage, cylinders=cylinders,
        airbags=airbags, cat=cat, li=li, fuel=fuel, gear=gear, wheel=wheel, turbo=turbo
    )

    prediction = model.predict(X_new)[0]
    st.success(f"Predicted Price: ${prediction:,.2f}")