# Import necessary libraries
import pandas as pd
import os

# Set file paths
train_file = os.path.join(os.getcwd(), "train.csv")
test_file = os.path.join(os.getcwd(), "test.csv")

# Load datasets
train_data = pd.read_csv(train_file)
test_data = pd.read_csv(test_file)

# Explore training data
print("Training Data Info:")
print(train_data.info())
print("\nFirst 5 rows of Training Data:")
print(train_data.head())

print("\nMissing Values in Training Data:")
print(train_data.isnull().sum())

print("\nDate Range in Training Data:")
print(train_data['date'].min(), "to", train_data['date'].max())

print("\nNumber of Duplicate Rows in Training Data:")
print(train_data.duplicated().sum())

# Explore testing data
print("\nTesting Data Info:")
print(test_data.info())
print("\nFirst 5 rows of Testing Data:")
print(test_data.head())






# Convert 'date' column to datetime in both datasets
train_data['date'] = pd.to_datetime(train_data['date'])
test_data['date'] = pd.to_datetime(test_data['date'])

# Verify the changes
print("\nDate column type in Training Data:")
print(train_data['date'].dtypes)




# Check for missing values
print("\nMissing Values in Training Data:")
print(train_data.isnull().sum())

# If there are missing values, decide on a strategy (example: drop rows with missing values)
train_data.dropna(inplace=True)

# Verify no missing values remain
print("\nMissing Values After Cleaning:")
print(train_data.isnull().sum())



# Remove duplicate rows
train_data.drop_duplicates(inplace=True)

# Verify the number of duplicates removed
print("\nNumber of Duplicate Rows After Cleaning:")
print(train_data.duplicated().sum())



# Create new columns for year, month, and day
train_data['year'] = train_data['date'].dt.year
train_data['month'] = train_data['date'].dt.month
train_data['day'] = train_data['date'].dt.day
train_data['day_of_week'] = train_data['date'].dt.dayofweek

# Preview the new columns
print("\nTraining Data with New Features:")
print(train_data.head())

# Data Cleaning and Preparation
# Convert 'date' to datetime
train_data['date'] = pd.to_datetime(train_data['date'])
test_data['date'] = pd.to_datetime(test_data['date'])

# Handle missing values
train_data.dropna(inplace=True)

# Remove duplicates
train_data.drop_duplicates(inplace=True)

# Feature engineering: Add year, month, day, and day_of_week
train_data['year'] = train_data['date'].dt.year
train_data['month'] = train_data['date'].dt.month
train_data['day'] = train_data['date'].dt.day
train_data['day_of_week'] = train_data['date'].dt.dayofweek

# Verify changes
print("\nTraining Data After Cleaning and Preparation:")
print(train_data.head())


