import streamlit as st
import cv2
import numpy as np
from PIL import Image

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("Image Processing Using DSA")

st.write("Upload an image and apply different algorithms.")

# ---------------------------------------------------
# IMAGE UPLOAD
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

# ---------------------------------------------------
# PROCESS IMAGE
# ---------------------------------------------------
if uploaded_file is not None:

    # Convert uploaded file to image
    image = Image.open(uploaded_file)

    image = np.array(image)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    # ---------------------------------------------------
    # SELECT OPERATION
    # ---------------------------------------------------
    option = st.selectbox(
        "Choose Processing Operation",
        (
            "Grayscale",
            "Blur",
            "Edge Detection",
            "Negative Image",
            "Brightness Increase"
        )
    )

    # ---------------------------------------------------
    # GRAYSCALE
    # ---------------------------------------------------
    if option == "Grayscale":

        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        st.subheader("Grayscale Image")

        st.image(gray, use_container_width=True)

    # ---------------------------------------------------
    # BLUR
    # ---------------------------------------------------
    elif option == "Blur":

        kernel = np.ones((3, 3), np.float32) / 9

        blurred = cv2.filter2D(image, -1, kernel)

        st.subheader("Blurred Image")

        st.image(blurred, use_container_width=True)

    # ---------------------------------------------------
    # EDGE DETECTION
    # ---------------------------------------------------
    elif option == "Edge Detection":

        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        edges = cv2.Canny(gray, 100, 200)

        st.subheader("Edge Detected Image")

        st.image(edges, use_container_width=True)

    # ---------------------------------------------------
    # NEGATIVE IMAGE
    # ---------------------------------------------------
    elif option == "Negative Image":

        negative = 255 - image

        st.subheader("Negative Image")

        st.image(negative, use_container_width=True)

    # ---------------------------------------------------
    # BRIGHTNESS
    # ---------------------------------------------------
    elif option == "Brightness Increase":

        value = st.slider(
            "Select Brightness",
            0,
            100,
            30
        )

        bright = cv2.convertScaleAbs(
            image,
            alpha=1,
            beta=value
        )

        st.subheader("Brightness Increased Image")

        st.image(bright, use_container_width=True)