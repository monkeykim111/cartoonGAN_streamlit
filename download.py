import streamlit as st

# from skimage import io
from input import *

import cv2


def imdown(image):
    if st.button("Download"):
        st.write("Downloading...")

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite("cartoonize.jpeg", image)  # opencv는 BGR로 반대라 색이 이상함

        st.write("Finish downloading!")

