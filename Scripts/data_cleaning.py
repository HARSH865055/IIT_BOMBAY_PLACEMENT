import pandas as pd
from pathlib import Path

# Step 1: Find project folder
project_folder = Path(__file__).resolve().parent.parent

# Step 2: Load dataset
file_path = project_folder / "Dataset" / "iit_bombay_placement_data.csv"
df = pd.read_csv(file_path)

# Step 3: Display original data information
print("Original Dataset Shape:", df.shape)

# Step 4: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Step 6: Remove duplicate records
df = df.drop_duplicates()

# Step 7: Handle missing values
df = df.dropna()

# Step 8: Save cleaned dataset
output_file = project_folder / "Dataset" / "cleaned_placement_data.csv"
df.to_csv(output_file, index=False)

# Step 9: Display final results
print("\nCleaned Dataset Shape:", df.shape)
print("Data cleaning completed successfully!")
print("Saved at:", output_file)
