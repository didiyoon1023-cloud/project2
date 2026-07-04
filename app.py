import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="컴퓨터와 가위바위보 한판!", page_icon="✊")

# 2. 디자인 적용 (배경색: 연분홍, 글자색: 검정)
st.markdown(
    """
    <style>
    /* 전체 배경 연분홍 */
    .stApp {
        background-color: #FFF0F5 !important;
    }
    /* 모든 텍스트 까만색 */
    h1, h2, h3, p, span, div, label {
        color: #000000 !important;
    }
    /* 버튼 스타일 커스텀 */
    .stButton button {
        background-color: #FFFFFF !important;
        border: 1px solid #ffb6c1 !important;
        border-radius: 10px !important;
    }
    /* 버튼 위 글자색 까만색 고정 */
    .stButton button p {
        color: #000000 !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. 세션 스테이트 초기화 (화면 단계 관리)
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'result' not in st.session_state:
    st.session_state.result = None

# --- [페이지 1: 메인 화면] ---
if st.session_state.page == 'main':
    st.title("컴퓨터
