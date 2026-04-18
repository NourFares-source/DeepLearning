import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Load the artifacts we just created
model = joblib.load('melbourne_rf_model.pkl')
scaler = joblib.load('scaler.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("🏠 Melbourne House Price Predictor")

# 2. Input UI
rooms = st.slider("Number of Rooms", 1, 10, 3)
distance = st.number_input("Distance from CBD (km)", 0.0, 50.0, 10.0)
landsize = st.number_input("Landsize (m²)", 0, 10000, 500)
building_area = st.number_input("Building Area (m²)", 0, 5000, 150)
year_built = st.number_input("Year Built", 1800, 2026, 1970)

region = st.selectbox("Select Region", [
    'Southern Metropolitan', 'Northern Metropolitan', 'Western Metropolitan', 
    'Eastern Metropolitan', 'South-Eastern Metropolitan', 'Eastern Victoria', 
    'Northern Victoria', 'Western Victoria'
])

# 3. Prediction logic
if st.button("Calculate Price"):
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Map inputs to the right columns
    input_df['Rooms'] = rooms
    input_df['Distance'] = distance
    input_df['Landsize'] = landsize
    input_df['BuildingArea'] = building_area
    input_df['YearBuilt'] = year_built
    
    region_col = f"Regionname_{region}"
    if region_col in model_columns:
        input_df[region_col] = 1
        
    # Scale and predict
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    
    st.header(f"Estimated Value: ${prediction:,.2f}")
