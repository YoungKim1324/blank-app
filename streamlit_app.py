# 스트림릿 라이브러리 가져오기
import streamlit as st

# 앱 제목
st.title("간단한 스트림릿 웹 앱")

# 사용자 입력 받기
user_input = st.text_input("메시지를 입력하세요:")

# 입력된 메시지 출력하기
if user_input:
    st.write(f"입력하신 메시지: {user_input}")
