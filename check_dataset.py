import pandas as pd

# Load dataset
data = pd.read_csv("dataset/kc_house_data.csv")

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nColumn names:")
print(data.columns.tolist())

print("\nMissing values:")
print(data.isnull().sum()) 