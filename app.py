
import streamlit as st

st.set_page_config(page_title="Universal ERP", layout="wide")
st.title("🌍 Universal ERP Dashboard")

st.write("Welcome to your Universal ERP system! Choose a module from the sidebar.")

st.sidebar.header("📊 Modules")
module = st.sidebar.radio("Select Module", ["Sales", "Procurement", "Inventory", "Finance", "Analytics"])

if module == "Sales":
    st.header("🛒 Sales Module")
    st.write("This is where you manage leads and customers.")

elif module == "Procurement":
    st.header("📦 Procurement Module")
    st.write("Find and compare suppliers here.")

elif module == "Inventory":
    st.header("📦 Inventory Module")
    st.write("Track and update stock here.")

elif module == "Finance":
    st.header("💰 Finance Module")
    st.write("See reports and financial summaries.")

elif module == "Analytics":
    st.header("📈 Analytics Module")
    st.write("Visualize KPIs and trends.")
