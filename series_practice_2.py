import pandas as pd

dates = ["2023-11-01", "2023-11-02", "2023-11-03", "2023-11-04", "2023-11-05", "2023-11-06", "2023-11-07", "2023-11-08", "2023-11-09", "2023-11-10"]
sales = [320, 400, 350, 380, 420, 360, 390, 410, 430, 410]

# Creating a Pandas Series with dates as the index
book_sales_series = pd.Series(data=sales, index=dates)
print(book_sales_series)

