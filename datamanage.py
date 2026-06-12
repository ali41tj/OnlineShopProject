import sqlite3
import pandas as pd


class DatabaseManager:

    def __init__(self):

        self.conn = sqlite3.connect("store_database.db")

    def get_sales_by_category(self):

        query = """
        SELECT
            category,
            SUM(quantity) AS total_quantity
        FROM orders
        GROUP BY category
        """

        return pd.read_sql_query(
            query,
            self.conn
        )

    def get_top_products(self):

        query = """
        SELECT
            product,
            SUM(quantity) AS total_quantity
        FROM orders
        GROUP BY product
        ORDER BY total_quantity DESC
        LIMIT 5
        """

        return pd.read_sql_query(
            query,
            self.conn
        )

    def get_orders_by_city(self):

        query = """
        SELECT
            city,
            COUNT(*) AS total_orders
        FROM orders
        GROUP BY city
        """

        return pd.read_sql_query(
            query,
            self.conn
        )

    def get_orders_per_customer(self):

        query = """
        SELECT
            customer_id,
            COUNT(*) AS total_orders
        FROM orders
        GROUP BY customer_id
        ORDER BY total_orders DESC
        LIMIT 15
        """

        return pd.read_sql_query(
            query,
            self.conn
        )

    def get_monthly_sales(self):

        query = """
        SELECT
            substr(order_date,1,7) AS month,
            SUM(quantity) AS total_sales
        FROM orders
        GROUP BY month
        ORDER BY month
        """

        return pd.read_sql_query(
            query,
            self.conn
        )

    def get_customer_behavior(self):

        query = """
        SELECT
            o.customer_id,
            o.quantity,
            o.price,
            u.signup_date
        FROM orders o
        JOIN users u
        ON o.customer_id = u.user_id
        """

        return pd.read_sql_query(
            query,
            self.conn
        )

    def close(self):

        self.conn.close()

print(DatabaseManager.get_customer_behavior())