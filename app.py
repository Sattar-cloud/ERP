# Universal ERP System Architecture with Web Interface (Streamlit)

import requests
from bs4 import BeautifulSoup
import streamlit as st

class SalesBot:
    def generate_leads(self):
        urls = ["https://www.alibaba.com", "https://www.made-in-china.com"]
        leads = []
        headers = {"User-Agent": "Mozilla/5.0"}
        for url in urls:
            try:
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                for company in soup.find_all('div', class_='company-info'):
                    leads.append(company.text.strip())
            except Exception as e:
                leads.append(f"Error accessing {url}: {e}")
        return leads if leads else ["No leads found."]

class ProcurementBot:
    def compare_suppliers(self, product_name):
        url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={product_name}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            suppliers = []
            for item in soup.find_all('div', class_='organic-gallery-title'):
                suppliers.append(item.text.strip())
            return suppliers if suppliers else ["No suppliers found."]
        except Exception as e:
            return [f"Error fetching suppliers: {e}"]

class InventoryBot:
    inventory = {}

    def update_stock(self, sku, delta):
        self.inventory[sku] = self.inventory.get(sku, 0) + delta
        return self.inventory[sku]

    def forecast_demand(self):
        return {"forecast": "Stable for next quarter"}

class FinanceBot:
    def generate_reports(self):
        return {
            "P&L": "Positive",
            "Balance Sheet": "Balanced"
        }

class AnalyticsBot:
    def kpi_dashboard(self):
        return {
            "revenue": "$120,000",
            "profit_margin": "30%",
            "shipment_delays": "2%"
        }

class ERPSystem:
    def __init__(self):
        self.sales = SalesBot()
        self.procurement = ProcurementBot()
        self.inventory = InventoryBot()
        self.finance = FinanceBot()
        self.analytics = AnalyticsBot()

erp = ERPSystem()

st.set_page_config(page_title="Universal ERP", layout="wide")
st.title("🌍 Universal ERP Dashboard")

st.sidebar.header("📊 Select a Module")
module = st.sidebar.radio("Choose Module", ["Sales & Leads", "Procurement", "Inventory", "Finance", "Analytics"])

if module == "Sales & Leads":
    st.header("🔍 Lead Generation")
    st.write("Click to fetch fresh business leads from trade websites.")
    if st.button("Generate Leads"):
        leads = erp.sales.generate_leads()
        st.success("Leads successfully retrieved!")
        for i, lead in enumerate(leads[:10], 1):
            st.write(f"{i}. {lead}")

elif module == "Procurement":
    st.header("📦 Supplier Search")
    st.write("Find global suppliers for your product.")
    product = st.text_input("Enter Product Name", "LED Light")
    if st.button("Find Suppliers"):
        suppliers = erp.procurement.compare_suppliers(product)
        st.success("Supplier list fetched!")
        for i, supplier in enumerate(suppliers[:10], 1):
            st.write(f"{i}. {supplier}")

elif module == "Inventory":
    st.header("📦 Inventory Manager")
    sku = st.text_input("Product SKU")
    delta = st.number_input("Change in Stock", step=1)
    if st.button("Update Stock"):
        if sku:
            result = erp.inventory.update_stock(sku, delta)
            st.success(f"Updated stock for {sku}: {result}")
        else:
            st.error("SKU cannot be empty.")
    if st.button("Forecast Demand"):
        forecast = erp.inventory.forecast_demand()
        st.info(forecast)

elif module == "Finance":
    st.header("💰 Financial Reports")
    st.write("View current financial performance.")
    if st.button("Generate Reports"):
        report = erp.finance.generate_reports()
        st.json(report)

elif module == "Analytics":
    st.header("📈 KPI Dashboard")
    if st.button("Show KPIs"):
        kpis = erp.analytics.kpi_dashboard()
        st.metric(label="Revenue", value=kpis["revenue"])
        st.metric(label="Profit Margin", value=kpis["profit_margin"])
        st.metric(label="Shipment Delays", value=kpis["shipment_delays"])
import streamlit as st

st.set_page_config(page_title="Universal ERP", layout="wide")

st.title("🌐 Universal ERP Dashboard")
st.write("Welcome! This is your AI-powered ERP system for global trade automation.")
