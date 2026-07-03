import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")

# Input numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Select operation
operation = st.selectbox(
    "Select Operation",
    (
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Sin",
        "Cos",
        "Tan",
        "Log",
        "Factorial"
    )
)

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero.")
            else:
                result = num1 / num2

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Square Root":
            if num1 < 0:
                st.error("Square root of a negative number is not possible.")
            else:
                result = math.sqrt(num1)

        elif operation == "Sin":
            result = math.sin(math.radians(num1))

        elif operation == "Cos":
            result = math.cos(math.radians(num1))

        elif operation == "Tan":
            result = math.tan(math.radians(num1))

        elif operation == "Log":
            if num1 <= 0:
                st.error("Log is only defined for positive numbers.")
            else:
                result = math.log10(num1)

        elif operation == "Factorial":
            if num1 < 0 or int(num1) != num1:
                st.error("Factorial is only defined for non-negative integers.")
            else:
                result = math.factorial(int(num1))

        if 'result' in locals():
            st.success(f"Result = {result}")

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.write("Created using Python & Streamlit")