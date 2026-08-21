import pandas as pd

# Load internship dataset
internships = pd.read_csv("data/internships.csv")

print("Dataset loaded successfully!")

# Display dataset
print(internships)

# Dataset dimensions
print("\nDataset shape:")
print(internships.shape)

# Column names
print("\nColumn names:")
print(internships.columns)

# Missing values
print("\nMissing values:")
print(internships.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(internships.duplicated().sum())

# Dataset information
print("\nDataset information:")
internships.info()

# Create a copy for cleaning
cleaned_internships = internships.copy()

# Remove duplicate rows
cleaned_internships = cleaned_internships.drop_duplicates()

# Remove unnecessary spaces from text
for column in cleaned_internships.select_dtypes(include="object").columns:
    cleaned_internships[column] = cleaned_internships[column].str.strip()

# Display cleaned dataset
print("\nCleaned dataset:")
print(cleaned_internships.head())

# Save cleaned dataset
cleaned_internships.to_csv(
    "data/cleaned_internships.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")