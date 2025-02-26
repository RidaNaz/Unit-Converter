import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from conversion import conversion_categories

load_dotenv()

# Initialize the Gemini model
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Streamlit app

# Set page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="favicon.ico"
)

# Sidebar for selecting conversion category
st.sidebar.title("Conversion Categories")
selected_category = st.sidebar.selectbox("Select a category:", list(conversion_categories.keys()))

# Dynamic title based on selected category
st.markdown(f"<h1 style='color: green; font-weight: bold;'>{selected_category} Converter</h1>",unsafe_allow_html=True)
st.markdown("Smart unit conversions—fast, accurate, and AI-driven!")

# Get the units for the selected category
unit_conversions = conversion_categories[selected_category]

# Layout for From and To units with amounts
col1, col2 = st.columns(2)

with col1:
    st.subheader("From")
    amount = st.number_input("Amount:", min_value=0.0, format="%.2f", key="from_amount")
    from_unit = st.selectbox("Unit:", list(unit_conversions.keys()), key="from_unit")

with col2:
    st.subheader("To")
    result_amount = st.text_input("Result:", value=st.session_state.get("conversion_result", ""), disabled=True, key="to_amount")
    to_unit = st.selectbox("Unit:", unit_conversions.get(from_unit, []), key="to_unit")

# Conversion prompt
prompt = ChatPromptTemplate.from_template(
    "Convert {amount} {from_unit} to {to_unit}. Provide only the numeric result with the unit.")

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