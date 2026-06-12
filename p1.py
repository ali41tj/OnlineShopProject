import sqlite3
import pandas as pd


users_df = pd.read_csv('users.csv')
orders_df = pd.read_csv('orders.csv')

conn = sqlite3.connect("store_database.db")

users_df.to_sql('users', conn, if_exists='replace', index=False)
orders_df.to_sql('orders', conn, if_exists='replace', index=False)


conn.close()









































conn.close()
