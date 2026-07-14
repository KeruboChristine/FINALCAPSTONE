import streamlit as st
import pandas as pd
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib 


# =========================================================
# 1. LOAD THE EXACT EXPORTED TRAINING ASSETS
# =========================================================
@st.cache_resource
def load_lstm_assets():
    model = None
    scaler = None
    
    custom_objects = {
        'mse': tf.keras.losses.MeanSquaredError(),
        'MeanSquaredError': tf.keras.losses.MeanSquaredError()
    }
    
    model_options = ["LSTM_Model.h5", "lstm_model.h5", "Lstm_Model.h5", "LSTM_Model.keras", "lstm_model.keras"]
    for option in model_options:
        if os.path.exists(option):
            model = load_model(option, custom_objects=custom_objects, compile=False)
            break
            
    scaler_options = ["MinMax_Scaler.pkl", "minmax_scaler.pkl", "Minmax_Scaler.pkl", "scaler.pkl", "Scaler.pkl"]
    for option in scaler_options:
        if os.path.exists(option):
            scaler = joblib.load(option)
            break
            
    return model, scaler

# FIXED: Initialize the variable to False by default
assets_loaded = False

try:
    st.sidebar.info(f"📂 Current App Directory: `{os.getcwd()}`")
    
    lstm_model, training_scaler = load_lstm_assets()
    
    if lstm_model is None or training_scaler is None:
        missing_components = []
        if lstm_model is None: missing_components.append("Model (.h5)")
        if training_scaler is None: missing_components.append("Scaler (.pkl)")
        
        all_files = os.listdir(".")
        matching_files = [f for f in all_files if "model" in f.lower() or "scaler" in f.lower() or ".h5" in f or ".pkl" in f]
        
        raise FileNotFoundError(f"Missing components: {', '.join(missing_components)}. Found these related files: {matching_files}")
    
    # FIXED: Explicitly set to True when loading succeeds
    assets_loaded = True
except Exception as e:
    st.error(f"❌ Asset loading error!\n\n{e}")
    assets_loaded = False

# =========================================================
# 2. PAGE CONFIGURATION & SIDEBAR DESIGN
# =========================================================
st.set_page_config(page_title="Food Security Prediction", page_icon="🔮", layout="centered")
st.title("🔮 Food Security LSTM Deep Learning Dashboard")
st.markdown("Predict the next month's fractional IPC food security classification using historical time-series lags.")

st.sidebar.header("🔮 Time-Series Inputs")
st.sidebar.markdown("Provide the continuous historical IPC indices for the selected region.")

# Load locations dynamically from dataset if present
DATA_PATH = "food_security_model_ready.csv" 
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    unique_locations = df['geographic_unit_name'].unique().tolist()
else:
    unique_locations = ["Western High Potential Zone", "Northeastern Pastoral Zone", "Central Highlands", "Aberdare Forest 1"]

selected_location = st.sidebar.selectbox("Geographic Unit Name", unique_locations)

st.sidebar.markdown("---")
st.sidebar.subheader("3-Month Sliding Window History")

# Collect the exact 3 lookback steps your model was trained on
lag_3 = st.sidebar.number_input("IPC Value 3 Months Ago (t-3)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
lag_2 = st.sidebar.number_input("IPC Value 2 Months Ago (t-2)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
lag_1 = st.sidebar.number_input("Previous Month IPC Value (t-1)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)

# =========================================================
# 3. REAL-TIME PREDICTION ENGINE
# =========================================================
if st.sidebar.button("🚀 Run Prediction Analysis"):
    
    if not assets_loaded:
        st.error("Prediction halted: Missing required model or scaler components.")
    else:
        # 1. Arrange history into chronological training sequence order: [t-3, t-2, t-1]
        raw_sequence = np.array([[lag_3], [lag_2], [lag_1]]) # Shape: (3, 1)
        
        # 2. Normalize inputs using your fitted training data bounds to fix saturation
        try:
            scaled_sequence = training_scaler.transform(raw_sequence) # Shape: (3, 1)
        except Exception as scale_err:
            st.error(f"Scaling failed. Check your scaler dimensions: {scale_err}")
            st.stop()
            
        # 3. Reshape scaled sequence to fit 3D LSTM architecture: [samples=1, time_steps=3, features=1]
        lstm_input = scaled_sequence.reshape((1, 3, 1))
        
        # 4. Generate continuous evaluation prediction 
        scaled_prediction = lstm_model.predict(lstm_input)
        
        # 5. Inverse transform predictions back to real-world 1.0 - 5.0 index scale
        real_prediction = float(training_scaler.inverse_transform(scaled_prediction.reshape(-1, 1))[0, 0])
        
        # Clip outputs edge-case boundaries safely between 1.0 and 5.0
        real_prediction = max(1.0, min(5.0, real_prediction))

        # 6. Display Clean Metric Metrics Results
        st.markdown("### 📊 Calculated Analysis Result")
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.metric("Predicted Continuous IPC Score (t)", f"{real_prediction:.2f}")
            st.caption(f"Target node: {selected_location}")
            
        with res_col2:
            if real_prediction < 1.5:
                st.success("**Phase 1: Minimal Security** 🟢")
            elif real_prediction < 2.5:
                st.info("**Phase 2: Stressed System** 🟡")
            elif real_prediction < 3.5:
                st.warning("**Phase 3: Food Crisis** 🟠")
            elif real_prediction < 4.5:
                st.error("**Phase 4: Emergency Alert** 🔴")
            else:
                st.error("**Phase 5: Famine Catastrophe** 💀")
                
        st.success("✅ Real-time inference executed successfully using your optimized training pipeline components!")
