import pandas as pd

# Load dataset
df = pd.read_csv("dataset/simulated_crowd_data.csv")

# Display first five records
print("\nFIRST FIVE RECORDS")
print(df.head())

# Display last five records
print("\nLAST FIVE RECORDS")
print(df.tail())

# Dataset dimensions
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Dataset information
print("\nDATASET INFORMATION")
df.info()

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Count records by location
print("\nLOCATION COUNTS")
print(df["location"].value_counts())

# Crowd-density distribution
print("\nCROWD DENSITY DISTRIBUTION")
print(df["crowd_density"].value_counts())

