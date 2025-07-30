import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")

# Load the model dictionary
with open("rainfall_prediction_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
features = model_data["feature_names"]

st.set_page_config(page_title="Rainfall Prediction", layout="centered")
st.title("🌧 Rainfall Prediction")
st.markdown("Provide today's weather information to predict whether there will be **rainfall or not**.")

st.sidebar.header("Enter Weather Details")
def user_input_features():
    inputs = {}
    inputs["pressure"] = st.sidebar.number_input("Pressure (hPa)", value=1010.0)
    inputs["dewpoint"] = st.sidebar.number_input("Dew Point (°C)", value=18.0)
    inputs["humidity"] = st.sidebar.number_input("Humidity (%)", value=80)
    inputs["cloud"] = st.sidebar.number_input("Cloud Cover (%)", value=70)
    inputs["sunshine"] = st.sidebar.number_input("Sunshine (hours)", value=5.0)
    inputs["winddirection"] = st.sidebar.number_input("Wind Direction (degrees)", value=90.0)
    inputs["windspeed"] = st.sidebar.number_input("Wind Speed (km/h)", value=20.0)
    return pd.DataFrame([inputs])

input_df = user_input_features()

# Display user input
st.subheader("Your Input")
st.write(input_df)

# Predict
try:
    input_df = input_df[features]  # Ensure correct column order
    prediction = model.predict(input_df)[0]
    result = "🌧️ Rainfall Expected" if prediction == 1 else "☀️ No Rainfall"
    st.subheader("Prediction Result")
    st.success(result)
except Exception as e:
    st.error("❌ Prediction failed. Check input format.")
    st.code(str(e))
