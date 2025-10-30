import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import random

# Dashboard Title
st.title("Smart Waste Management Dashboard")
st.write("This line confirms Streamlit is rendering.")

# Model Loading with Error Handling
MODEL_PATH = "waste_classifier_model.h5"

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    st.success("Model loaded successfully.")
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

# Waste labels (update if you train on different classes)
LABELS = ['Plastic', 'Paper', 'Metal']

# Waste Image Classification
st.header("Upload Waste Image for Classification")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def preprocess_image(img):
    # Ensure PIL image (convert from upload file if needed)
    if isinstance(img, io.BytesIO):
        img = Image.open(img)
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    if img_array.shape[-1] == 4:  # PNG with alpha
        img_array = img_array[..., :3]
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Waste Image", use_column_width=True)
    img_array = preprocess_image(img)
    try:
        predictions = model.predict(img_array)
        pred_label = LABELS[np.argmax(predictions)]
        confidence = np.max(predictions)
        st.write(f"**Predicted Waste Type:** {pred_label} (Confidence: {confidence:.2f})")
    except Exception as e:
        st.error(f"Failed to predict: {e}")

# Bin Status Simulation
st.header("Bin Status & Alerts (Simulated)")
bins = {
    "Bin A": random.randint(40, 100),
    "Bin B": random.randint(30, 90),
    "Bin C": random.randint(50, 100)
}

for bin_name, level in bins.items():
    st.write(f"{bin_name}: Level = {level}%")
    if level > 80:
        st.warning(f"Alert! {bin_name} is full and needs emptying.")

st.info("Dashboard and model are working! If you see this, everything is loading.")
