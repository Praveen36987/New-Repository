import streamlit as st
import joblib

# Load trained model
model = joblib.load("demand_model.pkl")

st.title("🏠 House Price Prediction App")

area = st.number_input("Enter the area (sq ft):", min_value=500, max_value=10000, step=100)

if st.button("Predict Price"):
    prediction = model.predict([[area]])
    st.success(f"Estimated Price: ₹{prediction[0]:,.0f}")
