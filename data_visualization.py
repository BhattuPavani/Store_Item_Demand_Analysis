# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the path for the training dataset
train_file = os.path.join(os.getcwd(), "train.csv")

# Load the dataset
train_data = pd.read_csv(train_file)

# Convert 'date' column to datetime
train_data['date'] = pd.to_datetime(train_data['date'])

# Feature engineering: Extract year, month, day, and day_of_week
train_data['year'] = train_data['date'].dt.year
train_data['month'] = train_data['date'].dt.month
train_data['day'] = train_data['date'].dt.day
train_data['day_of_week'] = train_data['date'].dt.dayofweek

# Ensure the data is ready
print("Data loaded and prepared for visualization!")



# Plot sales over time
plt.figure(figsize=(12, 6))
plt.plot(train_data['date'], train_data['sales'], label="Sales", color="blue")
plt.title("Sales Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()



# Aggregate sales by month
monthly_sales = train_data.groupby('month')['sales'].sum()

# Plot monthly sales
plt.figure(figsize=(8, 5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette="Blues_d")
plt.title("Total Sales by Month", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.show()


# Aggregate sales by store
store_sales = train_data.groupby('store')['sales'].sum()

# Plot sales by store
plt.figure(figsize=(8, 5))
sns.barplot(x=store_sales.index, y=store_sales.values, palette="Greens_d")
plt.title("Total Sales by Store", fontsize=16)
plt.xlabel("Store", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.show()


# Aggregate sales by day of the week
day_sales = train_data.groupby('day_of_week')['sales'].sum()

# Map day_of_week to actual days for better readability
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_sales.index = days

# Plot sales by day of the week
plt.figure(figsize=(8, 5))
sns.barplot(x=day_sales.index, y=day_sales.values, palette="Oranges_d")
plt.title("Total Sales by Day of the Week", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.show()
