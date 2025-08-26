import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV load
df = pd.read_csv('data/ecommerce_data.csv')  # अगर CSV same folder में है तो 'ecommerce_data.csv'

# First 5 rows
print(df.head())

# Total Sales calculate
df['Total_Sales'] = df['Quantity'] * df['Price']

# Category-wise total sales
category_sales = df.groupby('Category')['Total_Sales'].sum()
print("\nCategory wise total sales:")
print(category_sales)

# Plot: Total Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.show()
