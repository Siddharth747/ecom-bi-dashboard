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

# Total Revenue
q1 = "SELECT SUM(revenue) AS total_revenue FROM sales_data;"
df1 = pd.read_sql(q1, conn)
print("\n💰 Total Revenue: ")
print(df1)


# Total revenue by region
q2 = """
    SELECT region, SUM(revenue) AS total_revenue 
    FROM sales_data
    GROUP BY region
    ORDER BY total_revenue DESC;
"""
df2 = pd.read_sql(q2, conn)
print("\n🗺️ Revenue by region: ")
print(df2)
df2.plot(kind='bar', x='region', y='total_revenue', legend=False)
plt.title("Revenue by Region")
plt.ylabel('₹')
plt.tight_layout()
# plt.show()


# Top Selling Products
q3 = """
    SELECT product_name, SUM(quantity) AS total_sold
    FROM sales_data
    GROUP BY product_name
    ORDER BY total_sold DESC;
"""
df3 = pd.read_sql(q3, conn)
print("\n🏆 Winning Products")
print(df3)
df3.plot(kind='barh', x='product_name', y='total_sold', legend=False, color='green')
plt.title("Top Selling Products")
plt.xlabel("Units Sold")
plt.tight_layout()
plt.show()

# daily sales trend
q4 = """
    SELECT date, SUM(revenue) AS daily_revenue
    FROM sales_data
    GROUP BY date
    ORDER BY date;
"""
df4 = pd.read_sql(q4,conn)
print("\n🗓️ Daily Sales Trend: ")
print(df4)
df4.plot(kind='line', x='date', y='daily_revenue', marker='o', color='purple')
plt.title('Daily revenue Trend')
plt.ylabel('₹')
plt.tight_layout()
plt.show()

conn.close()