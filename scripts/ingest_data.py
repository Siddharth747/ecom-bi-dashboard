import psycopg2
import pandas as pd

df = pd.read_csv("../data/sales_data.csv")

try:
    conn = psycopg2.connect(
        dbname="ecom_bi", 
        user="postgres", 
        password="password",
        host="localhost",
        port="7474"
    )

    curr = conn.cursor()
    print("✅ DB connected")

    # Index Rows
    for index, row in df.iterrows():
        curr.execute(""" 
            INSERT INTO sales_data (date, product_name, quantity, revenue, region)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['date'], row['product_name'], row['quantity'], row['revenue'], row['region']))

        conn.commit()
        print("✅ Data Inserted Successfully!")

except Exception as e:
    print("❌ Error: ", e)

finally:
    curr.close()
    conn.close()
