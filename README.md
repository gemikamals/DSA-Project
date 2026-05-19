# Image Processing Using DSA

A simple Image Processing project built using **Python**, **Streamlit**, **OpenCV**, and **NumPy**.

This project allows users to upload an image and apply different image processing algorithms interactively through a web interface.

---

## Features

- Grayscale Conversion
- Blur Filter
- Edge Detection
- Negative Image
- Brightness Adjustment

---

## Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow (PIL)

---

## Project Structure

```text
DSA-Project/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/DSA-Project.git
```

Move into the project folder:

```bash
cd DSA-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
streamlit run app.py
```

---

## How It Works

1. Upload an image file (`jpg`, `png`, `jpeg`)
2. Select an image processing operation
3. View the processed output instantly

---

## Algorithms Used

### 1. Grayscale Conversion
Converts the uploaded image into grayscale format.

### 2. Blur Filter
Applies averaging filter using a 3×3 kernel matrix.

### 3. Edge Detection
Uses the Canny Edge Detection algorithm to detect edges.

### 4. Negative Image
Creates the negative of the image by inverting pixel values.

### 5. Brightness Increase
Adjusts image brightness using scaling operations.

---

## Future Improvements

- Add histogram equalization
- Add image compression
- Add webcam support
- Add AI-based image classification
- Improve UI design

---

## Author

Kamal Prajapat  
B.Tech Artificial Intelligence and Data Engineering  
Malaviya National Institute of Technology Jaipur

---

## License

This project is open-source and available under the MIT License.
