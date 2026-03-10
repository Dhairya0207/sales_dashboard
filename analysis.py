# import pandas as pd

# # read dataset
# df = pd.read_csv("data/train.csv")

# # show first 5 rows
# print(df.head())


# import pandas as pd

# df = pd.read_csv("data/train.csv")

# print("First 5 rows:")
# print(df.head())

# print("\nColumn names:")
# print(df.columns)

# print("\nDataset information:")
# print(df.info())

# print("\nSummary statistics:")
# print(df.describe())

import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")

print("First 5 rows:")
print(df.head())

# -----------------------------
# 1️⃣ Sales by Region
# -----------------------------
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

# -----------------------------
# 2️⃣ Sales by Category
# -----------------------------
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# -----------------------------
# 3️⃣ Top 10 Products
# -----------------------------
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products:")
print(top_products)

import matplotlib.pyplot as plt

# -----------------------------
# Bar Chart - Sales by Region
# -----------------------------
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.show()