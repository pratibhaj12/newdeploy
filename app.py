import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('multi_home_price_model.pkl')

# Title
st.title('HomePrices Prediction App')

# Input fields
area = st.number_input('Enter area (in square feet):', min_value=100.0, step=50.0)
bedrooms = st.number_input('Enter number of bedrooms:', min_value=1, step=1)
bathrooms = st.number_input('Enter number of bathrooms:', min_value=1, step=1)

# Prediction button
if st.button('Predict Price'):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)[0]
    st.success(f'Estimated Home Price: ₹{prediction:,.2f}')
