# import streamlit as st

# st.title("Calculator")

# # Input numbers
# a = st.number_input("Enter your first number:", step=1.0, format="%.4f")
# b = st.number_input("Enter your second number:", step=1.0, format="%.4f")

# # Operation selector
# operation = st.selectbox("Choose your calculating operation", ["/", "*", "+", "-", "**", "//", "%"])

# # Compute result
# result = None
# error = None

# if st.button("Calculate"):
#     if operation == "/" and b == 0:
#         error = "Error: Division by zero is not allowed."
#     elif operation == "//" and b == 0:
#         error = "Error: Division by zero is not allowed."
#     elif operation == "%" and b == 0:
#         error = "Error: Modulo by zero is not allowed."
#     else:
#         if operation == "/":
#             result = a / b
#         elif operation == "*":
#             result = a * b
#         elif operation == "+":
#             result = a + b
#         elif operation == "-":
#             result = a - b
#         elif operation == "**":
#             result = a ** b
#         elif operation == "//":
#             result = a // b
#         elif operation == "%":
#             result = a % b

# # Display output
# if error:
#     st.error(error)
# elif result is not None:
#     st.success(f"Result: {result}")
import streamlit as st

def calculate(num1, num2, operation):
    try:
        if operation == 'Add':
            return num1 + num2
        elif operation == 'Subtract':
            return num1 - num2
        elif operation == 'Multiply':
            return num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        elif operation == 'Power':
            return num1 ** num2
        elif operation == 'Root':
            if num2 == 0:
                return "Error: Zero root not defined"
            return num1 ** (1 / num2)
        elif operation == 'Percentage':
            return (num1 * num2) / 100
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.set_page_config(
        page_title="Professional Calculator",
        page_icon="🧮",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.markdown(
        """
        <style>
        .css-18e3th9 {
            padding-top: 3rem;
            padding-bottom: 3rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            height: 3rem;
            width: 100%;
            border-radius: 12px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🧮 Professional Calculator")
    st.write("Use this calculator to perform various mathematical operations with ease and precision.")

    with st.form(key='calc_form'):
        num1 = st.number_input("Enter first number", format="%.6f")
        num2 = st.number_input("Enter second number", format="%.6f")
        operation = st.selectbox("Select an operation", 
                                 ['Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Root', 'Percentage'])
        
        submit_button = st.form_submit_button(label='Calculate')
    
    if submit_button:
        result = calculate(num1, num2, operation)
        if isinstance(result, str) and result.startswith("Error:"):
            st.error(result)
        else:
            st.success(f"Result: {result}")

if __name__ == "__main__":
    main()

