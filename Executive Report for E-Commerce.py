import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading datasets
orders = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_orders_dataset.csv")
order_items = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_order_items_dataset.csv")
products = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_products_dataset.csv")
customers = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_customers_dataset.csv")
payments = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_order_payments_dataset.csv")
reviews = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_order_reviews_dataset.csv")
sellers = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_sellers_dataset.csv")
geo = pd.read_csv("C:/Users/Admin/Downloads/python dataset/olist_geolocation_dataset.csv")

#  Inspecting and Cleaning Datasets
print(orders.isnull().sum())
print(products.isnull().sum())
orders = orders.dropna(subset=['order_delivered_customer_date'])
products['product_category_name'] = products['product_category_name'].fillna('unknown')
orders = orders.drop_duplicates()
products = products.drop_duplicates()
date_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
             'order_delivered_customer_date', 'order_estimated_delivery_date']
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col])

#  Merging Datasets
order_customer = pd.merge(orders, customers, on='customer_id', how='left')
order_data = pd.merge(order_customer, order_items, on='order_id', how='left')
order_data = pd.merge(order_data, products, on='product_id', how='left')
order_data = pd.merge(order_data, payments, on='order_id', how='left')
order_data = pd.merge(order_data, reviews[['order_id', 'review_score']], on='order_id', how='left')

#  Feature Engineering
order_data['delivery_time_days'] = (
            order_data['order_delivered_customer_date'] - order_data['order_purchase_timestamp']).dt.days
order_data['estimated_delay'] = (
            order_data['order_delivered_customer_date'] - order_data['order_estimated_delivery_date']).dt.days
order_data['purchase_month'] = order_data['order_purchase_timestamp'].dt.month
order_data['purchase_year'] = order_data['order_purchase_timestamp'].dt.year

# Saving Cleaned Dataset
order_data.to_csv('cleaned_olist_data.csv', index=False)
print("Data cleaned and saved successfully.")


#  Summary Statistics
print("Summary Statistics:")
print(order_data.describe())
print("Data Types and Nulls:")
print(order_data.info())

# Analysis
plt.figure(figsize=(10, 6))
order_data['delivery_time_days'].plot.hist(bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Delivery Time (Days)')
plt.xlabel('Delivery Time (Days)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
order_data['estimated_delay'].plot.hist(bins=30, color='lightcoral', edgecolor='black')
plt.title('Distribution of Estimated Delivery Delay')
plt.xlabel('Estimated Delay (Days)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(order_data['estimated_delay'], order_data['delivery_time_days'], alpha=0.5, color='teal')
plt.title('Delivery Time vs Estimated Delay')
plt.xlabel('Estimated Delay (Days)')
plt.ylabel('Delivery Time (Days)')
plt.grid(True)
plt.tight_layout()
plt.show()


monthly_avg = order_data.groupby('purchase_month')['delivery_time_days'].mean()
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', color='mediumseagreen')
plt.title('Average Delivery Time by Purchase Month')
plt.xlabel('Month')
plt.ylabel('Average Delivery Time (Days)')
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()
plt.show()

corr_matrix = order_data[['delivery_time_days', 'estimated_delay', 'purchase_month']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

sns.boxplot(x='review_score', y='delivery_time_days', data=order_data)
plt.title('Delivery Time by Review Score')
plt.tight_layout()

plt.show()
