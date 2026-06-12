from nemodar.mat import DataAnalyzer
from clean.dataclean import DataCleann


analyzer = DataAnalyzer(
    "orders.csv",
    "users.csv"
)

cleaner = DataCleann(analyzer.df)

analyzer.df = cleaner.remove_duplicates()

analyzer.df = cleaner.fill_missing_prices()

analyzer.df = cleaner.fill_missing_city()

analyzer.df = cleaner.fix_negative_prices()

analyzer.df = cleaner.fix_quantity()

analyzer.df = cleaner.fix_price_outliers()


print("Cleaning Finished")
print(analyzer.df.head())


#analyzer.sales_by_category()

#analyzer.monthly_sales_trend()

#analyzer.top_products()

analyzer.orders_by_city()

#analyzer.price_distribution()

#analyzer.orders_per_customer()

analyzer.customer_behavior()