import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="1v1 미니 축구 게임", layout="wide")

st.title("⚽ 1대1 실시간 축구 게임")
st.caption("WASD / 방향키로 플레이하세요! 골이 들어가면 2초간 화면이 고정되며 화려한 GOAL 이펙트가 등장합니다.")

# 외부 HTML 파일 읽어오기
html_path = os.path.join(os.path.dirname(__file__), "game.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        game_html = f.read()
    components.html(game_html, height=780)
else:
    st.error("game.html 파일을 찾을 수 없습니다. main.py와 같은 폴더에 생성해 주세요.")
