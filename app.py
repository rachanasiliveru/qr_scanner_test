import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.set_page_config(page_title="QR Code Scanner", layout="centered")
st.title("📷 QR Code Scanner (OpenCV Version)")

uploaded_file = st.file_uploader("Upload an image with a QR code", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image using Pillow
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to OpenCV format (numpy array)
    image_cv = np.array(image)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

    # Initialize QRCodeDetector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    data, bbox, _ = detector.detectAndDecode(image_cv)

    if data:
        st.success("QR Code detected:")
        st.write(f"**Decoded Data:** {data}")
    else:
        st.warning("No QR code found in the image.")
