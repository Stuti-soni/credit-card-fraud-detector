import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Fraud Detector", page_icon="💳")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction data to check if it's fraudulent.")

# Load your trained model
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example features – replace/add as per your model
v1 = st.number_input("V1")
v2 = st.number_input("V2")
v3 = st.number_input("V3")
amount = st.number_input("Transaction Amount")

input_data = np.array([[v1, v2, v3, amount]])  # add more if your model needs

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("🚨 Fraud Detected!")
    else:
        st.success("✅ Legitimate Transaction")
