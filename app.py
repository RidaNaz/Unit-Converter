import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize the Gemini model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Streamlit app
st.title("Unit Converter")
st.markdown("Convert units in Length!")

# Unit options and their acceptable conversion units
unit_conversions = {
    "meters": ["kilometers", "feet", "yards", "miles", "inches"],
    "kilometers": ["meters", "miles"],
    "grams": ["kilograms", "pounds", "ounces"],
    "kilograms": ["grams", "pounds"],
    "liters": ["milliliters", "gallons"],
    "milliliters": ["liters"],
    "miles": ["kilometers", "meters", "feet", "yards"],
    "yards": ["meters", "feet", "inches", "miles"],
    "feet": ["meters", "yards", "inches", "miles"],
    "inches": ["meters", "feet", "yards"],
    "pounds": ["grams", "kilograms", "ounces"],
    "ounces": ["grams", "pounds"],
    "gallons": ["liters"]
}

col1, col2 = st.columns(2)

with col1:
    st.subheader("From")
    amount = st.number_input("Amount:", min_value=0.0, format="%.2f", key="from_amount")
    from_unit = st.selectbox("", list(unit_conversions.keys()), key="from_unit")

with col2:
    st.subheader("To")
    result_amount = st.text_input("Result:", value=st.session_state.get("conversion_result", ""), disabled=True, key="to_amount")
    to_unit = st.selectbox("", unit_conversions.get(from_unit, []), key="to_unit")

# Conversion prompt
prompt = ChatPromptTemplate.from_template(
    "Convert {amount} {from_unit} to {to_unit}. Provide only the numeric result.")

# Convert button
if st.button("Convert"):
    try:
        # Create the conversion chain
        chain = prompt | chat_model
        # Run the chain
        result = chain.invoke({
            "amount": amount,
            "from_unit": from_unit,
            "to_unit": to_unit
        })
        conversion_result = result.content if hasattr(result, "content") else str(result)
        # Store the result in session_state under a different key
        st.session_state.conversion_result = conversion_result
        st.rerun()
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")

# Display the result in green color and bold
if "conversion_result" in st.session_state:
    result_value = st.session_state.conversion_result
    st.markdown(
        f"<h3 style='color: green; font-weight: bold;'>Result: {result_value}</h3>",
        unsafe_allow_html=True
    )