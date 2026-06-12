import pandas as pd


class DataCleann:

    def __init__(self, dataframe):

        self.df = dataframe

    def remove_duplicates(self):

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        after = len(self.df)

        print(f"Removed {before - after} duplicate rows")

        return self.df

    def fill_missing_prices(self):

        avg_price = self.df["price"].mean()

        self.df["price"] = self.df["price"].fillna(avg_price)

        return self.df

    def fill_missing_city(self):

        self.df["city"] = self.df["city"].fillna("Unknown")

        return self.df

    def fix_negative_prices(self):

        avg_price = self.df.loc[
            self.df["price"] >= 0,
            "price"
        ].mean()

        self.df.loc[
            self.df["price"] < 0,
            "price"
        ] = avg_price

        return self.df

    def fix_quantity(self):

        avg_quantity = round(
            self.df.loc[
                self.df["quantity"] > 0,
                "quantity"
            ].mean()
        )

        self.df.loc[
            self.df["quantity"] <= 0,
            "quantity"
        ] = avg_quantity

        return self.df

    def fix_price_outliers(self):

        q1 = self.df["price"].quantile(0.25)

        q3 = self.df["price"].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - (1.5 * iqr)

        upper = q3 + (1.5 * iqr)

        avg_price = self.df.loc[
            (self.df["price"] >= lower) &
            (self.df["price"] <= upper),
            "price"
        ].mean()

        self.df.loc[
            (self.df["price"] < lower) |
            (self.df["price"] > upper),
            "price"
        ] = avg_price

        return self.df

    def show_missing_values(self):

        print(self.df.isnull().sum())

        