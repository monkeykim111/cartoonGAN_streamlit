import tensorflow as tf
import numpy as np
from PIL import Image
import streamlit as st


@st.cache
def cartoonize(content, model):
    # imported에다가 경로를 넣어줌 -> saved_model/GM
    imported = tf.saved_model.load(model)

    # 모델을 어떻게 적용할까?
    f = imported.signatures[
        "serving_default"
    ]  # f가 무엇인지 전혀 감이 안옴 / .signatures는 tensorflow 메소드 일 것
    img = np.array(content.convert("RGB"))
    # 업로드한 이미지를 Image를 통해 열고 convert RGB를 한다.

    img = np.expand_dims(img, 0).astype(np.float32) / 127.5 - 1
    out = f(tf.constant(img))["output_1"]
    out = ((out.numpy().squeeze() + 1) * 127.5).astype(np.uint8)
    return out


# 지금 모델을 읽지 못하고 있음
