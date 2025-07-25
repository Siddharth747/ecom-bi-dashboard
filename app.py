import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    dbname="ecom_bi",
    user="postgres",
    password="password",
    host="localhost",
    port="7474"
)

st.set_page_config(page_title="Ecom BI Dashboard", layout="wide")
st.title("Ecom CSV to Dashboard AI")
st.markdown("Track sales KPIs by region, product, and date")

df = pd.read_sql("SELECT * FROM sales_data", conn)

st.subheader("🔍 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{df['revenue'].sum():,.2f}")
col2.metric("Total Sales", int(df['quantity'].sum()))
col3.metric("Regions", df['region'].nunique())

st.subheader("Revenue by region")
regional_data = df.groupby("region")["revenue"].sum()
st.bar_chart(regional_data)

st.subheader("Top Selling Products")
revenue_data = df.groupby("product_name")["revenue"].sum()
st.bar_chart(revenue_data)

st.subheader("Daily Revenue Chart")
daily_Sellers = df.groupby("date")["revenue"].sum().sort_values(ascending=True)
st.bar_chart(daily_Sellers)