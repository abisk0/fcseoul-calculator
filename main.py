import streamlit as st
import math

st.set_page_config(
    page_title="Modern Calculator",
    page_icon="🧮",
    layout="centered"
)

# ------------------------
# CSS
# ------------------------
st.markdown("""
<style>

.stApp{
    background:#f3f4f6;
}

/* 제목 */
.title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#222;
    margin-bottom:25px;
}

/* 계산기 화면 */
.display{
    background:white;
    border-radius:18px;
    padding:20px;
    font-size:36px;
    font-weight:600;
    text-align:right;
    box-shadow:0 5px 15px rgba(0,0,0,.15);
    margin-bottom:25px;
    min-height:75px;
    overflow:hidden;
}

/* 버튼 */
.stButton>button{
    width:100%;
    height:95px;              /* 기존 70 → 95 */
    border-radius:18px;
    border:none;
    font-size:28px;           /* 기존 22 → 28 */
    font-weight:bold;
    background:#ffffff;
    color:#333;
    transition:all .2s ease;
    box-shadow:0 4px 10px rgba(0,0,0,.15);
}

/* Hover */
.stButton>button:hover{
    background:#4f8bf9;
    color:white;
    transform:translateY(-2px);
}

/* 클릭 효과 */
.stButton>button:active{
    transform:scale(0.96);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧮 Modern Calculator</div>', unsafe_allow_html=True)

# ------------------------
# Session State
# ------------------------
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "result" not in st.session_state:
    st.session_state.result = ""

# ------------------------
# Functions
# ------------------------
def add(char):
    st.session_state.expression += char

def clear():
    st.session_state.expression = ""
    st.session_state.result = ""

def back():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate():
    expr = st.session_state.expression.replace("^", "**")

    try:
        result = eval(expr)
        st.session_state.result = str(result)
        st.session_state.expression = str(result)
    except:
        st.session_state.result = "Error"

def log10():
    try:
        value = float(st.session_state.expression)
        result = math.log10(value)
        st.session_state.result = str(result)
        st.session_state.expression = str(result)
    except:
        st.session_state.result = "Error"

def ln():
    try:
        value = float(st.session_state.expression)
        result = math.log(value)
        st.session_state.result = str(result)
        st.session_state.expression = str(result)
    except:
        st.session_state.result = "Error"

def sqrt():
    try:
        value = float(st.session_state.expression)
        result = math.sqrt(value)
        st.session_state.result = str(result)
        st.session_state.expression = str(result)
    except:
        st.session_state.result = "Error"

# ------------------------
# Display
# ------------------------
display = st.session_state.expression if st.session_state.expression else "0"

st.markdown(
    f'<div class="display">{display}</div>',
    unsafe_allow_html=True
)

# ------------------------
# 버튼 배열
# ------------------------
rows = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="]
]

for row in rows:
    cols = st.columns(4, gap="small")

    for i, key in enumerate(row):
        with cols[i]:

            if st.button(key, use_container_width=True):

                if key == "C":
                    clear()

                elif key == "⌫":
                    back()

                elif key == "=":
                    calculate()

                else:
                    add(key)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------
# 과학 계산 버튼
# ------------------------
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    if st.button("log10", use_container_width=True):
        log10()

with col2:
    if st.button("ln", use_container_width=True):
        ln()

with col3:
    if st.button("√", use_container_width=True):
        sqrt()

# ------------------------
# 결과 표시
# ------------------------
if st.session_state.result != "":
    st.success(f"결과 : {st.session_state.result}")
