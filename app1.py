import streamlit as st
import pandas as pd
import numpy as np
import os
import datetime
import traceback
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import joblib 

# =========================================================
# 1. LOAD THE EXACT EXPORTED TRAINING ASSETS
# =========================================================
@st.cache_resource
def load_lstm_assets_safely():
    # A. Reconstruct your exact global notebook layer architecture manually
    # to completely defeat internal Keras .h5 header deserialization bugs.
    model = Sequential([
        LSTM(64, activation='tanh', input_shape=(3, 1), return_sequences=False),
        Dropout(0.1),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    
    # B. Locate and load your model weights file dynamically
    model_loaded = False
    model_options = ["LSTM_Model.h5", "lstm_model.h5", "Lstm_Model.h5", "LSTM_Model.keras", "lstm_model.keras"]
    for option in model_options:
        if os.path.exists(option):
            # FIXED: Removed by_name and skip_mismatch parameters to allow 
            # safe chronological/topological weight loading onto the cloud server.
            model.load_weights(option)
            model_loaded = True
            break
            
    # C. Locate and load your scaler file dynamically
    scaler = None
    scaler_options = ["MinMax_Scaler.pkl", "minmax_scaler.pkl", "Minmax_Scaler.pkl", "scaler.pkl", "Scaler.pkl"]
    for option in scaler_options:
        if os.path.exists(option):
            scaler = joblib.load(option)
            break
            
    if not model_loaded:
        return None, scaler
    return model, scaler

# Initialize baseline execution flag
assets_loaded = False

# Create visual containers for dashboard presentation
st.set_page_config(page_title="Food Security Prediction", page_icon="🔮", layout="centered")
st.title("🔮 Food Security LSTM Deep Learning Dashboard")
st.markdown("Predict the next month's fractional IPC food security classification using historical time-series lags.")

# Run asset pipeline setup check
try:
    lstm_model, training_scaler = load_lstm_assets_safely()
    
    if lstm_model is None or training_scaler is None:
        missing = []
        if lstm_model is None: missing.append("Model file (.h5)")
        if training_scaler is None: missing.append("Scaler file (.pkl)")
        all_files = os.listdir(".")
        raise FileNotFoundError(f"Missing pieces: {', '.join(missing)}. Available workspace files: {all_files}")
        
    assets_loaded = True
    st.success("✅ Clean model architecture built and training weights loaded smoothly!")

except Exception as load_error:
    st.error(f"❌ Asset Pipeline Verification Failed on Setup!")
    st.code(traceback.format_exc(), language="python")
    assets_loaded = False

# =========================================================
# 2. INTERFACE LAYOUT & SIDEBAR INPUTS
# =========================================================
st.sidebar.header("🔮 Control Panel")
st.sidebar.info(f"📂 Active Path: `{os.getcwd()}`\n\n🎯 Target Window: `(1, 3, 1)`")

DATA_PATH = "food_security_model_ready.csv" 
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    unique_locations = df['geographic_unit_name'].unique().tolist()
else:
    unique_locations = ["Western High Potential Zone", "Northeastern Pastoral Zone", "Central Highlands", "Aberdare Forest 1"]

selected_location = st.sidebar.selectbox("Geographic Unit Name", unique_locations)

st.sidebar.markdown("---")
st.sidebar.subheader("3-Month Sliding Window Lags")
lag_3 = st.sidebar.number_input("IPC Value 3 Months Ago (t-3)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
lag_2 = st.sidebar.number_input("IPC Value 2 Months Ago (t-2)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
lag_1 = st.sidebar.number_input("Previous Month IPC Value (t-1)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)

# =========================================================
# 3. RUNTIME PREDICTION ENGINE
# =========================================================
if st.sidebar.button("🚀 Run Prediction Analysis"):
    
    if not assets_loaded:
        st.error("🚨 Prediction halted: The application files are not initialized properly. Review the trace log error at the top of the main window.")
    else:
        try:
            # 1. Transform raw sequence metrics into standard uniform floats using .item()
            v3 = training_scaler.transform(np.array([[lag_3]])).item()
            v2 = training_scaler.transform(np.array([[lag_2]])).item()
            v1 = training_scaler.transform(np.array([[lag_1]])).item()
            
            sequence_list = [v3, v2, v1]
            
            # 2. Build the precise 3D shape array layout: (1 sample, 3 time steps, 1 feature)
            numpy_matrix = np.array(sequence_list, dtype=np.float32).reshape((1, 3, 1))
            tensor_input = tf.convert_to_tensor(numpy_matrix, dtype=tf.float32)
            
            # 3. Process raw forward prediction matrix pass
            raw_output = lstm_model(tensor_input, training=False)
            extracted_scalar = float(raw_output.numpy().flatten())
            
            # 4. Reverse normalization scaling back to standard 1.0 - 5.0 phase indices
            calculated_score = float(training_scaler.inverse_transform(np.array([[extracted_scalar]])))
            real_prediction = max(1.0, min(5.0, calculated_score))
            
            # 5. Output phase evaluation results panel
            st.markdown("### 📊 Continuous Prediction Performance Report")
            c1, c2 = st.columns(2)
            
            with c1:
                st.metric("Predicted Fractional IPC Score (t)", f"{real_prediction:.2f}")
                st.caption(f"Location Area: {selected_location}")
                st.caption(f"Array Target Map: `(1, 3, 1)`")
            with c2:
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
                    
            st.success("🎉 Calculation executed smoothly!")
            
        except Exception as prediction_error:
            st.error("❌ Runtime Calculation Breakdown!")
            st.code(traceback.format_exc(), language="python")
