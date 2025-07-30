# 🌧 Rainfall Prediction App

A machine learning web app that predicts whether **rainfall will occur or not** based on current weather conditions. Built using a **Random Forest Classifier** and deployed with **Streamlit**.


## 🚀 Features

- Interactive web interface using Streamlit
- Real-time prediction of rainfall (Yes/No)
- Uses key weather inputs: pressure, dewpoint, humidity, windspeed, etc.
- Cleaned and preprocessed weather dataset
- Easily extendable to support advanced models (e.g., XGBoost)


## 📊 Model Details

- Algorithm: `RandomForestClassifier`
- Target Variable: `rainfall` (`yes`/`no`)
- Input Features:
  - `pressure`
  - `dewpoint`
  - `humidity`
  - `cloud`
  - `sunshine`
  - `winddirection`
  - `windspeed`
