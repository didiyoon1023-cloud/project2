import streamlit as st
import math

# 1. 페이지 설정
st.set_page_config(page_title="일반/공학용 계산기", page_icon="🧮")

# 2. 강력한 CSS 인젝션 (하얀 배경, 검은 글씨, 주황색 특수 버튼)
st.markdown(
    """
    <style>
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
    }
    h1, h2, h3, p, span, div, label, .stMarkdown {
        color: #000000 !important;
    }
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
    .stButton button p {
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }
    .stButton button {
        background-color: #FFFFFF !important;
        border: 1px solid #DADCE0 !important;
        height: 60px !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
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
    st.session_state.display = "0"
if "reset_on_next" not in st.session_state:
    st.session_state.reset_on_next = False

# 버튼 입력 함수
def press(key):
    if st.session_state.reset_on_next and key not in ["+", "-", "×", "÷"]:
        st.session_state.display = ""
    st.session_state.reset_on_next = False
    
    if st.session_state.display == "0" or st.session_state.display == "Error":
        st.session_state.display = str(key)
    else:
        st.session_state.display += str(key)

# AC(초기화) 함수
def clear():
    st.session_state.display = "0"
    st.session_state.reset_on_next = False

# 백스페이스(◀) 함수
def backspace():
    if st.session_state.display in ["Error", "0"] or len(st.session_state.display) <= 1:
        st.session_state.display = "0"
    else:
        st.session_state.display = st.session_state.display[:-1]

# 등호(=) 및 결과 계산 함수
def calculate():
    try:
        expression = st.session_state.display.replace("×", "*").replace("÷", "/")
        result = eval(expression)
        if int(result) == result:
            result = int(result)
        st.session_state.display = str(result)
        st.session_state.reset_on_next = True
    except:
        st.session_state.display = "Error"
        st.session_state.reset_on_next = True

# 공학용 함수 계산기 전용 처리
def math_func(func_name):
    try:
        val = float(st.session_state.display)
        if func_name == "sqr":
            res = val ** 2
        elif func_name == "sqrt":
            res = math.sqrt(val)
        elif func_name == "sin":
            res = math.sin(math.radians(val))
        elif func_name == "cos":
            res = math.cos(math.radians(val))
        elif func_name == "tan":
            res = math.tan(math.radians(val))
            
        if int(res) == res:
            res = int(res)
        st.session_state.display = str(round(res, 6))
        st.session_state.reset_on_next = True
    except:
        st.session_state.display = "Error"
        st.session_state.reset_on_next = True

# 4. 상단 모드 전환 UI
mode = st.radio("계산기 모드 선택", ["일반 계산기", "공학용 계산기"], horizontal=True)

st.write("---")

# 5. 디스플레이 화면 렌더링
st.markdown(f'<div class="calc-display">{st.session_state.display}</div>', unsafe_allow_html=True)

# 6. 격자(Grid) 레이아웃 구성
if mode == "일반 계산기":
    row1 = st.columns(4)
    row2 = st.columns(4)
    row3 = st.columns(4)
    row4 = st.columns(4)
    row5 = st.columns(4)
    
    with row1[0]: st.markdown('<div class="orange-box">', unsafe_allow_html=True); st.button("AC", on_click=clear); st.markdown('</div>', unsafe_allow_html=True)
    with row1[1]: st.markdown('<div class="orange-box">', unsafe_allow_html=True); st.button("◀", on_click=backspace); st.markdown('</div>', unsafe_allow_html=True)
    with row1[2]: st.button(".", on_click=press, args=(".",))
    with row1[3]: st.button("÷", on_click=press, args=("÷",))
    
    with row2[0]: st.button("7", on_click=press, args=(7,))
    with row2[1]: st.button("8", on_click=press, args=(8,))
    with row2[2]: st.button("9", on_click=press, args=(9,))
    with row2[3]: st.button("×", on_click=press, args=("×",))
    
    with row3[0]: st.button("4", on_click=press, args=(4,))
    with row3[1]: st.button("5", on_click=press, args=(5,))
    with row3[2]: st.button("6", on_click=press, args=(6,))
    with row3[3]: st.button("-", on_click=press, args=("-",))
    
    with row4[0]: st.button("1", on_click=press, args=(1,))
    with row4[1]: st.button("2", on_click=press, args=(2,))
    with row4[2]: st.button("3", on_click=press, args=(3,))
    with row4[3]: st.button("+", on_click=press, args=("+",))
    
    with row5[0]: st.button("0", on_click=press, args=(0,))
    with row5[1]: st.button("00", on_click=press, args=("00",))
    with row5[2]: st.button("(", on_click=press, args=("(",))
    with row5[3]: st.button(")", on_click=press, args=(")",))
    
    st.write("")
    if st.button("=", use_container_width=True):
        calculate()

else:
    eng_row = st.columns(5)
    with eng_row[0]: st.button("x²", on_click=math_func, args=("sqr",))
    with eng_row[1]: st.button("√x", on_click=math_func, args=("sqrt",))
    with eng_row[2]: st.button("sin", on_click=math_func, args=("sin",))
    with eng_row[3]: st.button("cos", on_click=math_func, args=("cos",))
    with eng_row[4]: st.button("tan", on_click=math_func, args=("tan",))
    
    st.write("")
    
    row1 = st.columns(4)
    row2 = st.columns(4)
    row3 = st.columns(4)
    row4 = st.columns(4)
    row5 = st.columns(4)
    
    with row1[0]: st.markdown('<div class="orange-box">', unsafe_allow_html=True); st.button("AC", on_click=clear, key="eng_ac"); st.markdown('</div>', unsafe_allow_html=True)
    with row1[1]: st.markdown('<div class="orange-box">', unsafe_allow_html=True); st.button("◀", on_click=backspace, key="eng_back"); st.markdown('</div>', unsafe_allow_html=True)
    with row1[2]: st.button(".", on_click=press, args=(".",), key="eng_dot")
    with row1[3]: st.button("÷", on_click=press, args=("÷",), key="eng_div")
    
    with row2[0]: st.button("7", on_click=press, args=(7,), key="eng_7")
    with row2[1]: st.button("8", on_click=press, args=(8,), key="eng_8")
    with row2[2]: st.button("9", on_click=press, args=(9,), key="eng_9")
    with row2[3]: st.button("×", on_click=press, args=("×",), key="eng_mul")
    
    with row3[0]: st.button("4", on_click=press, args=(4,), key="eng_4")
    with row3[1]: st.button("5", on_click=press, args=(5,), key="eng_5")
    with row3[2]: st.button("6", on_click=press, args=(6,), key="eng_6")
    with row3[3]: st.button("-", on_click=press, args=("-",), key="eng_sub")
    
    with row4[0]: st.button("1", on_click=press, args=(1,), key="eng_1")
    with row4[1]: st.button("2", on_click=press, args=(2,), key="eng_2")
    with row4[2]: st.button("3", on_click=press, args=(3,), key="eng_3")
    with row4[3]: st.button("+", on_click=press, args=("+",), key="eng_add")
    
    with row5[0]: st.button("0", on_click=press, args=(0,), key="eng_0")
    with row5[1]: st.button("00", on_click=press, args=("00",), key="eng_00")
    with row5[2]: st.button("(", on_click=press, args=("(",), key="eng_open")
    with row5[3]: st.button(")", on_click=press, args=(")",), key="eng_close")
    
    st.write("")
    if st.button("=", use_container_width=True, key="eng_equal"):
        calculate()
