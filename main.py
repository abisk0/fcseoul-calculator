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

.title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#222;
    margin-bottom:25px;
}

.display{
    background:white;
    border-radius:15px;
    padding:18px;
    font-size:34px;
    text-align:right;
    box-shadow:0 3px 12px rgba(0,0,0,.12);
    margin-bottom:20px;
    min-height:70px;
    overflow:hidden;
}

.stButton>button{
    width:100%;
    height:70px;
    border-radius:14px;
    border:none;
    font-size:22px;
    font-weight:bold;
    background:#ffffff;
    color:#333;
    transition:0.2s;
    box-shadow:0 2px 5px rgba(0,0,0,.12);
}

.stButton>button:hover{
    background:#4f8bf9;
    color:white;
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
    expr = st.session_state.expression

    expr = expr.replace("^", "**")

    try:
        result = eval(expr)

        st.session_state.result = str(result)
        st.session_state.expression = str(result)

    except Exception:
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


# ------------------------
# Display
# ------------------------

display = st.session_state.expression

if display == "":
    display = "0"

st.markdown(
    f'<div class="display">{display}</div>',
    unsafe_allow_html=True
)

# ------------------------
# Button Layout
# ------------------------

rows = [
    ["C","⌫","%","/"],
    ["7","8","9","*"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","^","="]
]

for row in rows:

    cols = st.columns(4)

    for i,key in enumerate(row):

        with cols[i]:

            if st.button(key):

                if key == "C":
                    clear()

                elif key == "⌫":
                    back()

                elif key == "=":
                    calculate()

                else:
                    add(key)

# ------------------------
# Scientific Buttons
# ------------------------

st.write("")

col1,col2,col3 = st.columns(3)

with col1:

    if st.button("log10"):
        log10()

with col2:

    if st.button("ln"):
        ln()

with col3:

    if st.button("√"):

        try:

            value=float(st.session_state.expression)

            result=math.sqrt(value)

            st.session_state.expression=str(result)

            st.session_state.result=str(result)

        except:

            st.session_state.result="Error"

if st.session_state.result!="":
    st.success(f"결과 : {st.session_state.result}")
