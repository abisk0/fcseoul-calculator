import streamlit as st
import math

st.set_page_config(page_title="고급 계산기", page_icon="🧮")

st.title("🧮 고급 계산기")

# 연산 선택
operation = st.selectbox(
    "연산을 선택하세요",
    (
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러 연산",
        "지수 연산",
        "로그 연산"
    )
)

# 로그 연산은 입력 방식이 다름
if operation == "로그 연산":
    x = st.number_input("진수 x", value=10.0)
    base = st.number_input("밑(base)", value=10.0)

    if st.button("계산"):
        try:
            if x <= 0:
                st.error("진수는 0보다 커야 합니다.")
            elif base <= 0 or base == 1:
                st.error("밑은 0보다 크고 1이 아니어야 합니다.")
            else:
                result = math.log(x, base)
                st.success(f"결과: {result}")
        except Exception as e:
            st.error(f"오류 발생: {e}")

else:
    num1 = st.number_input("첫 번째 숫자", value=0.0)
    num2 = st.number_input("두 번째 숫자", value=0.0)

    if st.button("계산"):
        try:
            if operation == "덧셈":
                result = num1 + num2

            elif operation == "뺄셈":
                result = num1 - num2

            elif operation == "곱셈":
                result = num1 * num2

            elif operation == "나눗셈":
                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                    st.stop()
                result = num1 / num2

            elif operation == "모듈러 연산":
                if num2 == 0:
                    st.error("0으로 나눈 나머지는 계산할 수 없습니다.")
                    st.stop()
                result = num1 % num2

            elif operation == "지수 연산":
                result = num1 ** num2

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")
