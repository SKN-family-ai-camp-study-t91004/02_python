import streamlit as st

st.title("Media - image")

# 서버 이미지
st.image("../data/harden.jpeg", caption="harden")

# 웹 이미지
image_url = "https://www.chosun.com/resizer/v2/QTSLW42C4RGFPE2WEY2BTL22LE.jpg?auth=a5fa169f1ec8244c20235f8c27f98aefbf3e5366dd7362ee88bc206165fd57e7&width=616"
st.image(image_url, caption="웹 이미지")