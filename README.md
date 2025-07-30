## 🌧 Rainfall Prediction App

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


## Screenshots

![App Screenshot](https://i.postimg.cc/6q4NH1Gh/Screenshot-2025-07-30-214017.png)

![App Screenshot](https://i.postimg.cc/kMGM6TDG/Screenshot-2025-07-30-214033.png)

![App Screenshot](https://i.postimg.cc/bvYr6pYH/Screenshot-2025-07-30-214109.png)

![App Screenshot](https://i.postimg.cc/VN76ppdy/Screenshot-2025-07-30-214137.png)


## ⚙ How the Rainfall Prediction Model Works

This project uses a *Random Forest Classifier* to predict whether rainfall will occur (yes) or not (no) based on real-world weather conditions.

### 🔁 1. Data Preprocessing

- The raw dataset (Rainfall.csv) includes daily weather readings such as:
  - Atmospheric pressure, humidity, dew point, wind speed/direction, sunshine hours, etc.
- Irrelevant or redundant features like maxtemp, mintemp, and temparature were *removed*.
- Missing values were *dropped* to ensure model quality.
- The target column rainfall (values "yes"/"no") was encoded as:
  - "yes" → 1 (rainfall occurred)
  - "no" → 0 (no rainfall)

### 📊 2. Model Training

- A *RandomForestClassifier* from scikit-learn was trained on selected features:

['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed']

- The dataset was split into training and testing sets (e.g., 80/20).
- The model learns decision rules from the training data and builds multiple decision trees to make robust predictions.

### 🧠 3. Model Evaluation

- The model is evaluated using standard metrics:
- *Accuracy*
- *Precision*
- *Recall*
- *Confusion Matrix*
- Feature importance helps understand which inputs influence the prediction most.

### 🌐 4. Prediction via Streamlit App

- The trained model is saved as a .pkl file using pickle.
- The app takes user inputs (via sidebar) and converts them into a DataFrame.
- This input is passed to the model to predict whether it will rain or not:
- If model output is 1 → *🌧 Rainfall Expected*
- If model output is 0 → *☀ No Rainfall*
- The app runs locally or can be hosted on Streamlit Cloud.


## 📁 File Structure

├── Rainfall.csv                  # Dataset used
├── Rainfall_Prediction_ML.ipynb  # Model training + preprocessing
├── rainfall_prediction_model.pkl # Saved model
├── app.py                        # Streamlit web app
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation


---

## 📈 Future Improvements

Feature engineering: e.g., combining pressure and humidity

Try other ML models (e.g., XGBoost, LightGBM)

Cross-validation and hyperparameter tuning

Add probability output or feature importance plots

## 📬 Contact

Author: Farhan Abid

Email: farhanabidclass12@gmail.com

GitHub: farhanabid786
