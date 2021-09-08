import streamlit as st
import tensorflow as tf
from data import *
from input import image_input

st.title("SUDO권 조 발표")
st.sidebar.title("Tooning with CartoonGAN")

# 사용자가 selectbox에서 선택한 모델이 들어있는 객체
cartoon_model_name = st.sidebar.selectbox(
    "Select the cartoon model", cartoon_models_name
)

image_input(cartoon_model_name)

