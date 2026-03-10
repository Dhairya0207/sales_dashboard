import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")

df = pd.read_csv("Data/train.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

st.sidebar.header("Filters")

region_filter = st.sidebar.selectbox(
"Select Region",
["All"] + list(df["Region"].unique())
)

category_filter = st.sidebar.selectbox(
"Select Category",
["All"] + list(df["Category"].unique())
)

filtered_df = df.copy()

if region_filter != "All":
  filtered_df = filtered_df[filtered_df["Region"] == region_filter]

if category_filter != "All":
  filtered_df = filtered_df[filtered_df["Category"] == category_filter]

# KPIs

total_sales = filtered_df["Sales"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_customers = filtered_df["Customer Name"].nunique()
avg_sales = filtered_df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📦 Total Orders", total_orders)
col3.metric("👥 Customers", total_customers)
col4.metric("📈 Avg Order Value", f"${avg_sales:,.2f}")

# Charts Layout

col5, col6 = st.columns(2)

region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig1 = px.bar(region_sales, x="Region", y="Sales", title="Sales by Region")

col5.plotly_chart(fig1, use_container_width=True)

category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()

fig2 = px.pie(category_sales, values="Sales", names="Category", title="Sales by Category")

col6.plotly_chart(fig2, use_container_width=True)

# Monthly Trend

filtered_df["Month"] = filtered_df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()

fig3 = px.line(monthly_sales, x="Month", y="Sales", title="Monthly Sales Trend")

st.plotly_chart(fig3, use_container_width=True)

# Top Products

top_products = (
filtered_df.groupby("Product Name")["Sales"]
.sum()
.sort_values(ascending=False)
.head(10)
.reset_index()
)

fig4 = px.bar(
top_products,
x="Sales",
y="Product Name",
orientation="h",
title="Top 10 Products"
)

st.plotly_chart(fig4, use_container_width=True)

# Top Customers

top_customers = (
filtered_df.groupby("Customer Name")["Sales"]
.sum()
.sort_values(ascending=False)
.head(10)
.reset_index()
)

fig5 = px.bar(
top_customers,
x="Sales",
y="Customer Name",
orientation="h",
title="Top 10 Customers"
)

st.plotly_chart(fig5, use_container_width=True)
