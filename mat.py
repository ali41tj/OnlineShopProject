import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyzer:

    def __init__(self, orders_file, users_file):

        self.df = pd.read_csv(orders_file)
        self.df1 = pd.read_csv(users_file)

    def style_chart(self):

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        plt.tight_layout()

    # --------------------------------------------------

    def sales_by_category(self):

        t1 = self.df.groupby(
            "category"
        )["quantity"].sum()

        ax = t1.plot(
            kind="bar",
            figsize=(10, 6),
            color="skyblue",
            edgecolor="black"
        )

        plt.title(
            "Sales By Category",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel("Category")
        plt.ylabel("Quantity Sold")

        for p in ax.patches:

            ax.annotate(
                str(int(p.get_height())),
                (
                    p.get_x() + p.get_width() / 2,
                    p.get_height()
                ),
                ha="center",
                va="bottom"
            )

        self.style_chart()
        plt.show()

    # --------------------------------------------------

    def monthly_sales_trend(self):

        self.df["order_date"] = pd.to_datetime(
            self.df["order_date"]
        )

        t2 = (
            self.df.groupby(
                self.df["order_date"].dt.to_period("M")
            )["quantity"]
            .sum()
        )

        plt.figure(figsize=(10, 6))

        plt.plot(
            t2.index.astype(str),
            t2.values,
            marker="o",
            linewidth=3,
            markersize=8
        )

        plt.title(
            "Monthly Sales Trend",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel("Month")
        plt.ylabel("Sales")

        plt.xticks(rotation=45)

        plt.grid(
            linestyle="--",
            alpha=0.5
        )

        plt.tight_layout()
        plt.show()

    # --------------------------------------------------

    def top_products(self):

        t3 = (
            self.df.groupby("product")["quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        ax = t3.plot(
            kind="barh",
            figsize=(10, 6),
            color="orange",
            edgecolor="black"
        )

        plt.title(
            "Top 5 Products",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel("Units Sold")

        for p in ax.patches:

            ax.annotate(
                str(int(p.get_width())),
                (
                    p.get_width(),
                    p.get_y() + 0.3
                )
            )

        plt.tight_layout()
        plt.show()

    # --------------------------------------------------

    def orders_by_city(self):

        t4 = self.df["city"].value_counts()

        explode = [
            0.1 if i == 0 else 0
            for i in range(len(t4))
        ]

        plt.figure(figsize=(10, 10))

        plt.pie(
            t4,
            labels=t4.index,
            autopct="%1.1f%%",
            startangle=90,
            shadow=True,
            explode=explode
        )

        plt.title(
            "Orders By City",
            fontsize=18,
            fontweight="bold"
        )

        plt.tight_layout()
        plt.show()

    # --------------------------------------------------

    def price_distribution(self):

        plt.figure(figsize=(10, 6))

        plt.hist(
            self.df["price"],
            bins=15,
            edgecolor="black",
            alpha=0.7
        )

        plt.title(
            "Price Distribution",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel("Price")
        plt.ylabel("Frequency")

        plt.grid(
            linestyle="--",
            alpha=0.5
        )

        plt.tight_layout()
        plt.show()

    # --------------------------------------------------

    def orders_per_customer(self):

        t6 = (
            self.df["customer_id"]
            .value_counts()
            .head(15)
        )

        ax = t6.plot(
            kind="bar",
            figsize=(12, 6),
            color="lightgreen",
            edgecolor="black"
        )

        plt.title(
            "Top Customers By Number Of Orders",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel("Customer ID")
        plt.ylabel("Orders")

        for p in ax.patches:

            ax.annotate(
                str(int(p.get_height())),
                (
                    p.get_x() + p.get_width()/2,
                    p.get_height()
                ),
                ha="center"
            )

        self.style_chart()
        plt.show()

    # --------------------------------------------------

    def customer_behavior(self):

        self.df1["signup_date"] = pd.to_datetime(
            self.df1["signup_date"],
            format="mixed"
        )

        date_limit = pd.Timestamp(
            "2025-01-01"
        )

        merged = self.df.merge(
            self.df1,
            left_on="customer_id",
            right_on="user_id"
        )

        merged["total_sale"] = (
            merged["quantity"]
            * merged["price"]
        )

        before_sales = merged.loc[
            merged["signup_date"] < date_limit,
            "total_sale"
        ].sum()

        after_sales = merged.loc[
            merged["signup_date"] >= date_limit,
            "total_sale"
        ].sum()

        chart_data = pd.DataFrame({

            "Group": [
                "Before",
                "After"
            ],

            "Sales": [
                before_sales,
                after_sales
            ]
        })

        ax = chart_data.plot(
            x="Group",
            y="Sales",
            kind="bar",
            figsize=(8, 5),
            color=[
                "steelblue",
                "tomato"
            ],
            edgecolor="black"
        )

        plt.title(
            "Customer Behavior Before And After Signup Date",
            fontsize=14,
            fontweight="bold"
        )

        plt.ylabel(
            "Total Sales"
        )

        for p in ax.patches:

            ax.annotate(
                f"{int(p.get_height())}",
                (
                    p.get_x() + p.get_width()/2,
                    p.get_height()
                ),
                ha="center"
            )

        self.style_chart()
        plt.show()