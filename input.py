from data import *
import streamlit as st
from PIL import Image
from cartoonize import cartoonize
from download import imdown
import imutils


def image_input(cartoon_model_name):
    model = cartoon_models_dict[
        cartoon_model_name
    ]  # cartoon_model_name이 'GM'이라면 model에는 'saved_model/GM'가 담김
    content_file = st.sidebar.file_uploader(
        "Choose a Image to cartoonize!", type=["jpg", "png", "jpeg"]
    )  # 이미지를 업로드하고 그 이미지를 content_file 객체에 넣음

    if content_file is not None:
        content = Image.open(content_file)
        # 모델을 적용 --- cartoonize로 함수 만들기
        # 모델을 어떻게 적용을 시키지?? --- cartoonize.py에서 해결하기
        st.write("<Before Cartoonize>")
        st.image(content)

        st.write("<After Cartoonize>")
        generated = cartoonize(content, model)
        # generated에는 카툰화가 적용된 이미지가 담김
        st.image(generated)
        # 출력

        # 이미지 다운로드
        imdown(generated)
