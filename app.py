import streamlit as st
import math

# 1. 페이지 설정
st.set_page_config(page_title="일반/공학용 계산기", page_icon="🧮")

# 2. 강력한 CSS 인젝션 (하얀 배경, 검은 글씨, 주황색 특수 버튼)
st.markdown(
    """
    <style>
    /* 전체 배경 하얀색 */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
    }
    
    /* 일반 텍스트, 라디오 버튼 글씨 검은색 */
    h1, h2, h3, p, span, div, label, .stMarkdown {
        color: #000000 !important;
    }
    
    /* 계산기 디스플레이 스타일 */
    .calc-display {
        background-color: #F1F3F4;
        padding: 20px;
        border-radius: 10px;
        text-align: right;
        font-size: 2rem;
        font-weight: bold;
        color: #000000 !important;
        margin-bottom: 20px;
        border: 1px solid #DADCE0;
        min-height: 80px;
    }
    
    /* 모든 버튼 내부 텍스트 검은색 고정 및 마우스 올려도 유지 */
    .stButton button p {
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }
    
    /* 기본 버튼 배경 흰색 */
    .stButton button {
        background-color: #FFFFFF !important;
        border: 1px solid #DADCE0 !important;
        height: 60px !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
    
    /* AC와 백스페이스(◀) 버튼은 주황색 배경에 검은 글씨 */
    div[data-testid="column"]:nth-of-type(1) .stButton button.orange-btn,
    div[data-testid="column"]:nth-of-type(2) .stButton button.orange-btn,
    .orange-box button {
        background-color: #FF9F0A !important;
        border: 1px solid #CC7F08 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. 세션 스테이트(상태 관리) 초기화
if "display" not in st.session_state:
    st.session_state.display = "0"  # 화면에 표시될 수식 또는 결과
if "reset_on_next" not in st.session_state:
    st.session_state.reset_on_next = False  # 계산 완료 후 다음 입력 때 화면을 비울지 여부

# 버튼 입력 함수
def press(key):
    if st.session_state.reset_on_next and key not in ["+", "-", "×", "÷"]:
        st.session_state.display = ""  # <- 여기가 if문보다 안쪽으로 들여쓰기 되어야 해요!
    st.session_state.reset_on_next = False
    
    if st.session_state.display == "0" or st.session_state.display == "Error":
        st.session_state.display = str(key)
    else:
        st.session_state.display += str(key)
