import streamlit as st

st.title("Simple Calculator")

# Input numbers
a = st.number_input("Enter your first number:", step=1.0, format="%.4f")
b = st.number_input("Enter your second number:", step=1.0, format="%.4f")

# Operation selector
operation = st.selectbox("Choose your calculating operation", ["/", "*", "+", "-", "**", "//", "%"])

# Compute result
result = None
error = None

if st.button("Calculate"):
    if operation == "/" and b == 0:
        error = "Error: Division by zero is not allowed."
    elif operation == "//" and b == 0:
        error = "Error: Division by zero is not allowed."
    elif operation == "%" and b == 0:
        error = "Error: Modulo by zero is not allowed."
    else:
        if operation == "/":
            result = a / b
        elif operation == "*":
            result = a * b
        elif operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "**":
            result = a ** b
        elif operation == "//":
            result = a // b
        elif operation == "%":
            result = a % b

# Display output
if error:
    st.error(error)
elif result is not None:
    st.success(f"Result: {result}")
