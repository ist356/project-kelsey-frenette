import os
import pandas as pd

file_path = "cache/Parking Violations 2024.csv"

try:
    data = pd.read_csv(file_path)
    print("File loaded successfully!")
    print("Preview of the data:")
    print(data.head())  # Show the first few rows
except FileNotFoundError:
    print(f"File not found: {file_path}. Ensure the file exists in the 'cache' folder.")
