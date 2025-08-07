# Olist E-commerce Data Analysis and Demand Prediction

## 🔍 Project Overview
The project covers:
- Cleaning and merging multiple Olist datasets
- Feature engineering (delivery time, delay, etc.)
- Visualizing delivery trends, review scores, and category-wise metrics
- Predicting product demand using a Random Forest Classifier
- Power BI dashboard to interactively explore patterns

## 📁 Datasets Used
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_sellers_dataset.csv`
- `olist_geolocation_dataset.csv`
Source: [Olist Public Dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## 📊 Dashboard
An interactive Power BI dashboard includes:
- Delivery time distributions
- Estimated delays by month
- Review score trends
- Category-wise delivery insights
- Filter by year, review score, product category

## ⚙️ Tech Stack
- Python (pandas, matplotlib, seaborn, sklearn)
- Power BI for data visualization
- Jupyter Notebook / VSCode

## 🧠 Machine Learning
**Goal:** Predict product demand levels (low, medium, high) based on product & order features.
- Features used: price, freight, review score, product weight
- Model: Random Forest Classifier
- Accuracy metrics: Classification report included

## 📁 Output Files
- `cleaned_olist_data.csv`: Cleaned dataset after merging and feature engineering
- `demand_predictions.csv`: Includes demand level predictions
- `dashbord.pdf`: Dashboard visualizations (exported from Power BI)

## 🧪 How to Run
1. Clone the repo
2. Place all `.csv` files from the Olist dataset in the same folder
3. Run the Python script to clean data and generate predictions
4. Open `dashbord.pbix` in Power BI Desktop

## ✍️ Author
Fatima Ismail 
Data Analyst & Python Developer  
📧 Contact: [ismailf1286@gmail.com]

---

