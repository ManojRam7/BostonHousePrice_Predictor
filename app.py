import streamlit as st
import pickle
import numpy as np

# Load model and scaler
with open('regmodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaling.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit App
st.title('Boston House Price Predictor')

st.markdown("""
Provide the required inputs to predict the price of a house.
""")

# Input Fields
CRIM = st.number_input('CRIM (Per capita crime rate):', min_value=0.0)
ZN = st.number_input('ZN (Proportion of residential land):', min_value=0.0)
INDUS = st.number_input('INDUS (Non-retail business acres):', min_value=0.0)
CHAS = st.selectbox('CHAS (Charles River proximity):', [0, 1])
NOX = st.number_input('NOX (Nitric oxide concentration):', min_value=0.0)
RM = st.number_input('RM (Number of rooms):', min_value=0.0)
AGE = st.number_input('AGE (Proportion of older units):', min_value=0.0)
DIS = st.number_input('DIS (Weighted distance):', min_value=0.0)
RAD = st.number_input('RAD (Accessibility to highways):', min_value=0.0)
TAX = st.number_input('TAX (Property tax rate):', min_value=0.0)
PTRATIO = st.number_input('PTRATIO (Pupil-teacher ratio):', min_value=0.0)
B = st.number_input('B (1000(Bk - 0.63)^2):', min_value=0.0)
LSTAT = st.number_input('LSTAT (% lower status population):', min_value=0.0)

# Predict Button
if st.button('Predict'):
    # Prepare input for prediction
    input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)

    st.success(f'Estimated House Price: ${prediction[0]:,.2f}')
