import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize the Gemini model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Streamlit app
st.title("🌟 Google Unit Converter with Gemini AI")
st.markdown("Convert units seamlessly using AI-powered conversion!")

# Unit options
units = [
    "meters", "kilometers", "grams", "kilograms", "liters", "milliliters", 
    "miles", "yards", "feet", "inches", "pounds", "ounces", "gallons"
]

# Layout for From and To units with amounts
col1, col2 = st.columns(2)

with col1:
    st.subheader("From")
    amount = st.number_input("Amount:", min_value=0.0, format="%.2f", key="from_amount")
    from_unit = st.selectbox("Unit:", units, key="from_unit")

with col2:
    st.subheader("To")
    result_amount = st.text_input("Result:", value="", disabled=True, key="to_amount")
    to_unit = st.selectbox("Unit:", units, key="to_unit")

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
        st.session_state.to_amount = conversion_result
        st.experimental_rerun()
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")

# Update the result field
to_amount = st.session_state.get("to_amount", "")
st.text_input("Result:", value=to_amount, disabled=True, key="to_amount_display")